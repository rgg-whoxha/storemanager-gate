import logging
from typing import Any
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from exceptions import UserAlreadyExistsError, UserNotFoundError

logger = logging.getLogger(__name__)

class PermissionsRepository:
    def __init__(self, table):
        self.table = table

    def get_permissions_by_username(self, username: str) -> list[dict[str, Any]]:
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
    
    def update_permissions_by_username(self, username: str, permissions: list[str]) -> dict[str, Any]:
        try:
            response = self.table.update_item(
                Key={"username": username},
                UpdateExpression="SET #perms = :perms",
                ExpressionAttributeNames={"#perms": "permissions"},
                ExpressionAttributeValues={":perms": permissions},
                ReturnValues="UPDATED_NEW",
                ConditionExpression="attribute_exists(username)"
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
                raise UserNotFoundError(username)
            logger.error(
                "DB Error updating permissions for username %s: %s",
                username,
                err.response["Error"]["Message"]
            )
            raise err

    def create_user(self, username: str, permissions: list[str]) -> dict[str, Any]:
        try:

            self.table.put_item(
                Item={
                    "username": username,
                    "permissions": permissions if permissions else []
                },
                ConditionExpression="attribute_not_exists(username)"
            )
            return {
                "username": username,
                "permissions": permissions if permissions else []
            }
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
                # Expected conflict: user already exists
                raise UserAlreadyExistsError(username)
            logger.error(
                "DB Error creating user %s: %s",
                username,
                err.response["Error"]["Message"]
            )
            raise err
        
        
        
        