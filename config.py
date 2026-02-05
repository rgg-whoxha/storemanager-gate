import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AWS_REGION: str = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "local")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "local")
    DYNAMODB_ENDPOINT: str = os.getenv("DYNAMODB_ENDPOINT_URL", "http://localhost:8000")
    TABLE_NAME: str = "user_permissionsv2"

settings = Settings()