import os
_base_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_base_dir, "db.sqlite3")
SQLALCHEMY_MIGRATE_REPO = os.path.join(_base_dir, "migrations")

WTF_CSRF_ENABLED = True
SECRET_KEY = "insert-cool-secret-key-here"
