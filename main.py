from fastapi import FastAPI, HTTPException, Depends

from permissions_repository import PermissionsRepository
from exceptions import UserAlreadyExistsError, UserNotFoundError
from schemas import (
    CreateUserRequest, 
    CreateUserResponse,
    UpdatePermissionsRequest, 
    UpdatePermissionsResponse, 
    UserPermissionResponse
)
from database import get_db_table

app = FastAPI()

# Error messages
MSG_USERNAME_EMPTY = "Username cannot be empty"
MSG_USER_NOT_FOUND = "User not found"
MSG_USER_ALREADY_EXISTS = "User already exists"


def get_repository():
    table = get_db_table()
    return PermissionsRepository(table)

@app.get("/user/permissions", response_model=UserPermissionResponse)
def get_user_permissions(
    username: str,
    repo: PermissionsRepository = Depends(get_repository)
):
    if not username.strip():
        raise HTTPException(status_code=400, detail=MSG_USERNAME_EMPTY)
    
    items = repo.get_permissions_by_username(username)
    permissions = items[0].get("permissions", []) if items else []

    
    return UserPermissionResponse(
        username=username,
        permissions=permissions
    )
    
@app.put("/user/permissions", response_model=UpdatePermissionsResponse)
def update_user_permissions(
    request: UpdatePermissionsRequest, 
    repo: PermissionsRepository = Depends(get_repository)
):
    if not request.username.strip():
        raise HTTPException(status_code=400, detail=MSG_USERNAME_EMPTY)

    try:
        repo.update_permissions_by_username(request.username, request.permissions)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=MSG_USER_NOT_FOUND)
    
    return UpdatePermissionsResponse(
        username=request.username,
        permissions=request.permissions
    )

@app.post("/user", response_model=CreateUserResponse)
def create_user(
    request: CreateUserRequest,
    repo: PermissionsRepository = Depends(get_repository)
):
    if not request.username.strip():
        raise HTTPException(status_code=400, detail=MSG_USERNAME_EMPTY)
    
    try:
        created_user = repo.create_user(request.username, request.permissions)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail=MSG_USER_ALREADY_EXISTS)
    
    return CreateUserResponse(
        username=created_user.get("username", request.username),
        permissions=created_user.get("permissions", [])
    )
    