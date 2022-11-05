from aredis_om import get_redis_connection

from ..settings import get_settings

settings = get_settings()

keydb = get_redis_connection(decode_responses=True)
