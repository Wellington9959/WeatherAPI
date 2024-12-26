import redis
from redis.cache import CacheConfig

from src.configuration import settings

redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    protocol=3,
    cache_config=CacheConfig(),
    decode_responses=True,
)
