from fastapi import FastAPI, HTTPException, Depends

from permissions_repository import PermissionsRepository
from schemas import UserPermissionRequest, UserPermissionResponse
from database import get_db_table

app = FastAPI()


def get_repository():
    table = get_db_table()
    return PermissionsRepository(table)

@app.post("/user/permissions", response_model=UserPermissionResponse)
def get_user_permissions(
    request: UserPermissionRequest, 
    repo: PermissionsRepository = Depends(get_repository)
):
    if not request.username.strip():
        raise HTTPException(status_code=400, detail="Username cannot be empty")
    
    items = repo.get_permissions_by_username(request.username)
    permissions = [item["permission"] for item in items if "permission" in item]
    
    return UserPermissionResponse(
        user=request.username,
        permissions=permissions
    )
