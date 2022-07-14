import os
from dotenv import load_dotenv

load_dotenv()


class Constants:
    PORT = os.environ.get('PORT') or 8000
    DATABASE_URL = os.environ.get('DATABASE_URL') or ""
    PROD = os.environ.get('PROD') or None
    JWT_SECRET = os.environ.get('JWT_SECRET') or "SECRET"
    TOKEN_VALIDITY = os.environ.get('TOKEN_VALIDITY') or 7
    APP_NAME = os.environ.get('APP_NAME') or "APP"
