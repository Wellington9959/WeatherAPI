from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.configuration import settings

limiter = Limiter(
    get_remote_address,
    default_limits=[
        f"{settings.RATELIMIT_PER_DAY} per day",
        f"{settings.RATELIMIT_PER_HOUR} per hour",
    ],
    storage_uri=settings.REDIS_URL,
)
