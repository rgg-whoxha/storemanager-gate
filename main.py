from fastapi import FastAPI, HTTPException, Depends

from permissions_repository import PermissionsRepository
from schemas import UpdatePermissionsRequest, UpdatePermissionsResponse, UserPermissionRequest, UserPermissionResponse
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
    permissions = items[0].get("permissions", []) if items else []

    
    return UserPermissionResponse(
        username=request.username,
        permissions=permissions
    )
    
@app.put("/user/permissions", response_model=UpdatePermissionsResponse)
def update_user_permissions(
    request: UpdatePermissionsRequest, 
    repo: PermissionsRepository = Depends(get_repository)
):
    if not request.username.strip():
        raise HTTPException(status_code=400, detail="Username cannot be empty")

    
    repo.update_permissions_by_username(request.username, request.permissions)
    update_result = repo.update_permissions_by_username(request.username, request.permissions)
    if not update_result:
        raise HTTPException(status_code=404, detail="User not found")
    return UpdatePermissionsResponse(
        username=request.username,
        permissions=request.permissions
    )