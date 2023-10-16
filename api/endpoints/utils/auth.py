from datetime import datetime, timedelta

import jwt
from fastapi import Header, HTTPException, status
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import ValidationError

from models.user import User_Pydantic


SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'


def create_access_token(*, data: User_Pydantic, exp: int = None) -> bytes:
    to_encode = data
    if exp is not None:
        to_encode.update({'exp': exp})
    else:
        exp = 2400 
        # datetime.utcnow() + timedelta(minutes=60)
        to_encode.update({'exp': exp})

    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm='HS256'
    )
    return encoded_jwt


def get_user_from_header(*, authorization: str = Header(None)) -> User_Pydantic:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    scheme, token = get_authorization_scheme_param(authorization)
    if scheme.lower() != 'bearer':
        raise credentials_exception

    try:
        payload = jwt.decode(
            token, SECRET_KEY,
            algorithms=['HS256']
        )
        try:
            token_data = User_Pydantic(**payload)
            return token_data
        except ValidationError:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
