from fastapi import APIRouter, Depends
from typing import Annotated
from app.services.authentication import AuthService
router = APIRouter()


@router.post("/testjwt", response_description="Create a new user")
async def test_jwt(token: Annotated[str, Depends(AuthService.oauth2_bearer)]):
    username = await AuthService.get_current_user(token)
    return username


