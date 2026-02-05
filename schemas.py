from pydantic import BaseModel
from typing import List

class UserPermissionRequest(BaseModel):
    username: str

class UserPermissions(BaseModel):
    username: str
    permissions: List[str]

UserPermissionResponse = UserPermissions
UpdatePermissionsRequest = UserPermissions
UpdatePermissionsResponse = UserPermissions