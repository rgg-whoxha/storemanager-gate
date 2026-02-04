
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    email: str

@app.post("/user/permissions")
def get_permission_by_user_email(request: UserRequest):
    userEmail = request.email
    return {"user": userEmail}
