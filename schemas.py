from pydantic import BaseModel
from typing import List


class UserPermissions(BaseModel):
    username: str
    permissions: List[str]

UserPermissionResponse = UserPermissions
UpdatePermissionsRequest = UserPermissions
UpdatePermissionsResponse = UserPermissions
CreateUserRequest = UserPermissions
CreateUserResponse = UserPermissions