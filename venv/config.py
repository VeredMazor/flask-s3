import secrets

SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
SECRET_KEY = secrets.token_hex(16)