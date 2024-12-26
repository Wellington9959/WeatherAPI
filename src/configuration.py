import os

from dotenv import load_dotenv

load_dotenv()


class AppSettings:
    SERVER_NAME: str = os.getenv("SERVER_NAME", "0.0.0.0:5000")
    DEBUG: bool = os.getenv("DEBUG")  # Omit for False
    TESTING: bool = os.getenv("TESTING")  # Omit for False
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    REDIS_URL: str = os.getenv("REDIS_URL")
    CACHE_EXPIRY_SECONDS: int = os.getenv("CACHE_EXPIRY_SECONDS", 43200)  # default 12h

    RATELIMIT_ENABLED: bool = os.getenv("RATELIMIT_ENABLED")  # Omit for False
    RATELIMIT_PER_DAY: int = os.getenv("RATELIMIT_PER_DAY", 200)  # default 200/day
    RATELIMIT_PER_HOUR: int = os.getenv("RATELIMIT_PER_HOUR", 50)  # default 50/hour

    VISUALCROSSING_API_KEY: str = os.getenv("VISUALCROSSING_API_KEY")


settings = AppSettings()
