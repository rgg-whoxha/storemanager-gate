from config import settings
import boto3


dynamodb_resource = None


def _get_dynamodb_resource():
    """Lazily create and return the DynamoDB resource."""
    global dynamodb_resource
    if dynamodb_resource is None:
        dynamodb_resource = boto3.resource(
            'dynamodb',
            region_name=settings.AWS_REGION,
            endpoint_url=settings.DYNAMODB_ENDPOINT,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
    return dynamodb_resource


def get_db_table():
    """Helper to get the specific Table object"""
    return _get_dynamodb_resource().Table(settings.TABLE_NAME)
