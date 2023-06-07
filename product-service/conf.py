<<<<<<< HEAD
import os

from pydantic import BaseSettings

class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    GATEWAY_TIMEOUT: int = 59
=======
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    GATEWAY_TIMEOUT: int = 59
>>>>>>> 859e605 (changes to product-service)
settings = Settings()