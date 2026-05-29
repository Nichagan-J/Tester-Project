import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    DEFAULT_TIMEOUT = 10000
