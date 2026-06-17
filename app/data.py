"""
Single source of truth for all portfolio content.

Everything the templates render comes from here. To add a new work
experience, hobby, education entry, or map location, append a dict to the
relevant list below. The Jinja templates loop over these lists, so no HTML
changes are needed to add more items. This is what satisfies the Flask task:
"Add a template for adding multiple work experiences/education/hobbies using Jinja".
"""

# --- Basic identity, used across every page ---
PROFILE = {
    "name": "Gabriela",
    "tagline": "CS + Economics @ Notre Dame  ·  incoming Applied Digital Health @ Oxford",
    "location": "Toruń, Poland",
    "blurb": (
        "Builder working at the intersection of health, finance, and the "
        "humanities, and a sometime scholar of Dante and Italian visual "
        "culture."
    ),
    # Place your real photo at app/static/img/profile.jpg to replace the placeholder.
    "photo": "img/profile.jpg",
    "email": "you@example.com",
    "github": "https://github.com/your-username",
    "linkedin": "https://www.linkedin.com/in/your-handle",
}

# --- About section: a few paragraphs ---
ABOUT = [
    (
        "I'm finishing a dual degree in Computer Science and Economics at the "
        "University of Notre Dame and heading to Oxford for a master's in "
        "Applied Digital Health. My work tends to sit where rigorous systems "
        "meet messy human problems."
    ),
    (
        "Outside of building, I read and write about Italian literature and art "
        "history. My senior honors thesis reimagined Dante's Inferno through "
        "19th and 20th century art, and I care a lot about depth over breadth, "
        "whether that's a research question or a month in one country."
    ),
]

# --- Work experiences ---
WORK = [
    {
        "role": "MLH Fellow",
        "org": "Major League Hacking",
        "dates": "2026",
        "summary": (
            "Production Engineering track. Building open-source projects with "
            "engineers from top companies in a remote pod."
        ),
    },
]

# --- Education ---
EDUCATION = [
    {
        "degree": "MSc, Applied Digital Health",
        "school": "University of Oxford",
        "dates": "Incoming",
        "summary": "Graduate program at the intersection of health and technology.",
    },
    {
        "degree": "BS, Computer Science & Economics",
        "school": "University of Notre Dame",
        "dates": "Expected 2026",
        "summary": (
            "Dual degree. First Place, Hesburgh Libraries Research Award "
            "(Capstone/Thesis). Inducted into Gamma Kappa Alpha, the National "
            "Italian Honor Society. Senior honors thesis on Dante's Inferno in "
            "modern art."
        ),
    },
]

# --- Hobbies, each with an image ---
# Drop matching images into app/static/img/ to replace the placeholders.
HOBBIES = [
    {
        "name": "Freediving",
        "img": "img/hobby-freediving.jpg",
        "blurb": "Working toward certification. The discipline of one breath, one descent.",
    },
    {
        "name": "Italian literature & art history",
        "img": "img/hobby-italian.jpg",
        "blurb": "Dante, Boccaccio, the Baroque. Reading, writing, and the occasional museum pilgrimage.",
    },
    {
        "name": "Travel with depth",
        "img": "img/hobby-travel.jpg",
        "blurb": "One country, slowly. Local food, water, and culture over a checklist of sights.",
    },
]

# --- Map: places visited / lived ---
# lat/lng drive the Leaflet markers on the map page. Add a dict to add a pin.
PLACES = [
    {"name": "Toruń, Poland", "lat": 53.0138, "lng": 18.5984, "note": "Home."},
    {"name": "Notre Dame, USA", "lat": 41.7001, "lng": -86.2379, "note": "Undergrad."},
    {"name": "Oxford, UK", "lat": 51.7548, "lng": -1.2544, "note": "Master's, incoming."},
    {"name": "Amsterdam, NL", "lat": 52.3676, "lng": 4.9041, "note": "Currently passing through."},
    {"name": "Amed, Bali", "lat": -8.3389, "lng": 115.6878, "note": "Freediving certification."},
    {"name": "Tokyo, Japan", "lat": 35.6762, "lng": 139.6503, "note": "Trip bookend."},
]
