from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Settings:

    CURRENCY_PAIR_1: str = "GBP/RUB"
    CURRENCY_PAIR_2: str = "JPY/RUB"

    SMTP_USERNAME: str = getenv("SMTP_USERNAME")
    EMAIL_PASSWORD: str = getenv("EMAIL_PASSWORD")
    RECIPIENT_EMAIL: str = getenv("RECIPIENT_EMAIL")


settings = Settings()
