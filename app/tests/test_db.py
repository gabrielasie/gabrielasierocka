
import sys
import unittest
from pathlib import Path
from peewee import *

# Ensure `from app import ...` works even when tests are run from `app/`.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind the model to the app's in-memory database and create fresh
        # tables before each test.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        if test_db.is_closed():
            test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Drop tables after each test so tests stay isolated. The connection is
        # left open so other test modules sharing this database still work.
        test_db.drop_tables(MODELS)

    def test_timeline_post(self):
        # Create two posts to the database.
        first_post = TimelinePost.create(name="John Doe", email='jonh@example.com', 
                                         content='Hellow world, I\'m John!')
        assert first_post.id == 1
        
        second_post = TimelinePost.create(name="Jane Doe", email='jane@example.com', 
                                         content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # Retrieve the timeline posts and verify they were saved.
        posts = TimelinePost.select()
        assert posts.count() == 2

        # The application returns posts newest-first (created_at descending).
        ordered = list(
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        )
        assert ordered[0].name == "Jane Doe"
        assert ordered[1].name == "John Doe"


if __name__ == "__main__":
    unittest.main()