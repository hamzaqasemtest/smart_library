from fastapi import APIRouter, status
from datetime import timedelta
from app.routes.schemas.user import CreateUserReq, LoginRequest
from app.services.authentication import AuthService
from app.common.error_handling import UserAlreadyExistsException, RegistrationFailedException, InvalidCredentialsException

router = APIRouter()


@router.post("/register", response_description="Create a new user", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: CreateUserReq):
    auth_service = AuthService()

    # existed_user = await get_user_by_username( user_data.username)
    # if existed_user:
    #     raise UserAlreadyExistsException()

    user = await auth_service.register(user_data.username, user_data.password)
    if user:
        token = AuthService.create_access_token(
            username=user_data.username, expires_delta=timedelta(minutes=600)
        )
        return {"message": "registered successfully", "token": token}
    else:
        raise RegistrationFailedException()


@router.post("/login")
async def get_user(login_request: LoginRequest):
    auth_service = AuthService()
    user = await auth_service.login(login_request.username, login_request.password)
    # if user:
    #     token = create_access_token(
    #         username=login_request.username, expires_delta=timedelta(minutes=600)
    #     )
    #     return {"message": "Logged in successfully", "token": token}
    # else:
    #     raise InvalidCredentialsException()
