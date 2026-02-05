import logging
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)

class PermissionsRepository:
    def __init__(self, table):
        self.table = table

    def get_permissions_by_username(self, username: str):
        try:
            response = self.table.query(
                KeyConditionExpression=Key("username").eq(username)
            )
            return response.get("Items", [])
        except ClientError as err:
            logger.error(
                "DB Error querying username %s: %s",
                username,
                err.response["Error"]["Message"]
            )
            raise err