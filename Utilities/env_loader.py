import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Env:
    AWS_USERNAME = os.getenv("AWS_USERNAME")
    AWS_PASSWORD = os.getenv("AWS_PASSWORD")
    AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
    BASE_URL = os.getenv("BASE_URL")

    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_TO = os.getenv("EMAIL_TO")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT")
    EMAIL_BODY = os.getenv("EMAIL_BODY")

    @staticmethod
    def validate():
        required_vars = ["AWS_USERNAME", "AWS_PASSWORD", "AWS_ACCOUNT_ID"]
        for var in required_vars:
            if not os.getenv(var):
                raise EnvironmentError(f"{var} not set in environment variables!")
