import hashlib
from datetime import timezone, datetime, timedelta
from typing import Annotated
from fastapi import Depends
from config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError


class AuthService:

    oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


    @staticmethod
    def create_access_token(username: str, expires_delta: timedelta):
        encode = {"sub": username}
        expires = datetime.now(timezone.utc) + expires_delta
        encode.update({"exp": expires})
        return jwt.encode(encode, SECRET_KEY, ALGORITHM)



    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                #throw exception
                pass
            return {"username": username}
        except JWTError:
            # throw exception
            # Could not validate user
            pass

    async def register(self, username: str, password: str):
        pass

    async def login(self, username: str, password: str):
        pass


    @staticmethod
    def hash_password(password):
        sha_signature = hashlib.sha256(password.encode()).hexdigest()
        return sha_signature
