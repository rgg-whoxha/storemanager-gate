from pydantic import BaseModel
from typing import List

class UserPermissionRequest(BaseModel):
    username: str

class UserPermissionResponse(BaseModel):
    user: str
    permissions: List[str]