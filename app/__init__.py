import os
import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request
from peewee import *
from playhouse.shortcuts import model_to_dict

from . import data

load_dotenv()

app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

print(mydb)

# Anything secret/configurable comes from the environment, never hardcoded.
# See example.env. This satisfies the "use environment variables" tip.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-change-me")


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


# The navbar renders from this list. (endpoint, label) pairs.
# Add a tuple here and the link shows up in the menu on every page.
PAGES = [
    ("index", "Home"),
    ("about", "About"),
    ("work", "Work"),
    ("projects", "Projects"),
    ("education", "Education"),
    ("skills", "Skills"),
    ("hobbies", "Hobbies"),
    ("places", "Map"),
]


@app.context_processor
def inject_globals():
    # Makes these available to every template without passing them each time.
    return {"profile": data.PROFILE, "pages": PAGES}


@app.route("/")
def index():
    return render_template("index.html", about=data.ABOUT)


@app.route("/about")
def about():
    return render_template("about.html", about=data.ABOUT, honors=data.HONORS)


@app.route("/work")
def work():
    return render_template("work.html", work=data.WORK)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=data.PROJECTS)


@app.route("/education")
def education():
    return render_template(
        "education.html", education=data.EDUCATION, publications=data.PUBLICATIONS
    )


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=data.SKILLS)


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", hobbies=data.HOBBIES)


@app.route("/places")
def places():
    return render_template("places.html", places=data.PLACES)


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_time_line_post(post_id):
    deleted = TimelinePost.delete().where(TimelinePost.id == post_id).execute()
    if deleted == 0:
        return {"error": "post not found"}, 404
    return {"deleted": post_id}