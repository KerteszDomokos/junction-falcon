PRODUCTION = False

DATABASE_NAME = None if PRODUCTION else "database_name"

SQLALCHEMY_DATABASE_URI = (
    "add_connection_URI"
    + DATABASE_NAME
)
SESSION_TOKEN_SALT = "session_salt_here"

DATA_MAX_INTERVAL_LENGTH_SECONDS = 10 * 24 * 3600  # 90 days




