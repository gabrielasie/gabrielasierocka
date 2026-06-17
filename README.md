# Portfolio Site

Personal portfolio built with Flask for the MLH Fellowship, Week 1.

Live content is driven entirely from one file (`app/data.py`), so adding a job,
hobby, education entry, or map pin is a one-line change with no HTML edits.

## Tasks completed

**Portfolio**
- [x] Photo on the home page
- [x] About section (home preview + dedicated page)
- [x] Work experiences
- [x] Hobbies with images, on their own page
- [x] Education
- [x] Map of places visited (Leaflet + OpenStreetMap, no API key)

**Flask**
- [x] Runs locally (instructions below)
- [x] Multiple work/education/hobby entries rendered via Jinja loops over `data.py`
- [x] Dedicated hobbies page
- [x] Navbar that builds itself from the app's page list (`PAGES` in `app/__init__.py`)

## Stack

Flask, Jinja2 templates with inheritance, vanilla CSS, Leaflet for the map.
No database; content lives in `app/data.py`.

## Project layout

```
app/
  __init__.py        Flask app, routes, and the PAGES list the navbar reads
  data.py            All content. Edit this to make the site yours.
  static/
    css/style.css
    img/             Your photos go here
  templates/
    base.html        Shared layout + dynamic navbar
    index.html  about.html  work.html  education.html  hobbies.html  places.html
example.env          Copy to .env
requirements.txt
```

## Installation

Make sure you have python3 and pip installed.

```
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Create a `.env` file using the `example.env` template, then:

```
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

Open `localhost:5000` in the browser.

## Making it yours

1. Edit `app/data.py`: name, blurb, work, education, hobbies, and map pins.
2. Replace the placeholder images in `app/static/img/` with your own
   (`profile.jpg` and the `hobby-*.jpg` files).
3. To add a page: add a route in `app/__init__.py`, add a tuple to `PAGES`,
   and create a template that extends `base.html`. It appears in the nav automatically.

## Notes on secrets

`SECRET_KEY` is read from the environment via `python-dotenv`. `.env` is
gitignored so nothing sensitive is committed.
