from typing import Optional
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Request, HTTPException, Depends
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from typing import Annotated
from .config import settings

ALGORITHM = "HS256"


class JWTBearer(HTTPBearer):
    def __init__(self, **kwargs):
        super(JWTBearer, self).__init__(*kwargs)

    async def __call__(self, request: Request) -> Optional[str]:
        credentials: Optional[HTTPAuthorizationCredentials] = await super(JWTBearer, self).__call__(request)
        if credentials is None:
            return None
        try:
            payload = jwt.decode(
                credentials,
                settings.SECRET_KEY,
                algorithms=[ALGORITHM],
                options={"require": ["exp", "sub"]}
            )
        except ExpiredSignatureError:
            raise HTTPException(status_code=403, detail="Expired token.")
        except InvalidTokenError:
            raise HTTPException(status_code=403, detail="Invalid token.")
        return payload

class Security_Key(HTTPBearer):
    def __init__(self, *, bearerFormat = None, scheme_name = None, description = None, auto_error = True):
        super().__init__(bearerFormat=bearerFormat, scheme_name=scheme_name, description=description, auto_error=auto_error)

class APIKeyBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        credentials: HTTPAuthorizationCredentials | None = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=401, detail="Invalid authentication"
                )
            if credentials.credentials != settings.ROOT_KEY:
                raise HTTPException(
                    status_code=401, detail="Invalid authentication"
                )
            return credentials.credentials  # API key จะอยู่ใน credentials.credentials
        raise HTTPException(
            status_code=401, detail="Invalid or missing credentials."
        )

api_key_scheme = APIKeyBearer()

api_key_token = Annotated[str, Depends(api_key_scheme)]

async def api_key_route(api_key: Annotated[str, Depends(api_key_scheme)]):
    return {"api_key": api_key}