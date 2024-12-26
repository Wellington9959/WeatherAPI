import os

from dotenv import load_dotenv

load_dotenv()


class AppSettings:
    SERVER_NAME: str = os.getenv("SERVER_NAME")  # eg. "0.0.0.0:5000"
    DEBUG: bool = os.getenv("DEBUG")  # Omit for False
    TESTING: bool = os.getenv("TESTING")  # Omit for False
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    REDIS_URL: str = os.getenv("REDIS_URL")
    CACHE_EXPIRY_SECONDS: int = os.getenv("CACHE_EXPIRY_SECONDS")  # default 12h

    VISUALCROSSING_API_KEY: str = os.getenv("VISUALCROSSING_API_KEY")


settings = AppSettings()
