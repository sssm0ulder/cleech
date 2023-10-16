import json

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from schemas.telegram import TelegramUser
from models.user import User_Pydantic, UserIn_Pydantic, Users
from .utils.auth import create_access_token, get_user_from_header


router = APIRouter()

@router.post('/api/auth')
async def auth_for_telegram_users(data: UserIn_Pydantic):
    is_created_user = await Users.filter(user_id=data.user_id).first()

    if is_created_user:
        await is_created_user.update_from_dict({
            'first_name': data.first_name,
            'last_name': data.last_name,
            'tg_hash': data.tg_hash,
        }).save()

        user = await Users.filter(user_id=data.user_id).first()
    else:
        user_obj = await Users.create(**data.dict(exclude_unset=True))
        user = await User_Pydantic.from_tortoise_orm(user_obj)


    user = {
        'first_name': user.first_name,
        'last_name': user.last_name, 
        'tg_hash': user.tg_hash,
        'username': user.username,
        'user_id': user.user_id,
        'token_type': 'bearer',
    }
    token = create_access_token(data=user)
    user['token'] = token

    return JSONResponse(
        content={'data': user},
        status_code=status.HTTP_200_OK
    )


@router.get('/me')#, response_model=User_Pydantic)
def read_profile(user: User_Pydantic = Depends(get_user_from_header)):
    print(user)

    return {}
