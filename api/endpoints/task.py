from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from .utils.validators import TelegramURLValidator
from schemas.telegram import ConditionData, TaskData, TelegramUser
from models.user import Users
from models.task import Tasks
from tasks.telegram import check_user_in_channel_task


router = APIRouter()


@router.post('/api/telegram/check')
def check_user_conditions(data: ConditionData):
    url_validator = TelegramURLValidator(data.link)
    if url_validator.validate():
        is_subscribed = check_user_in_channel_task(
            channel_id=url_validator.get_channel_id(),
            user_id=data.user_id
        )
        if is_subscribed:
            return JSONResponse(
                content={'task_id': 'hash'},
                status_code=status.HTTP_200_OK
            )
        return JSONResponse(
            content={'message': 'User not subscribed'},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return JSONResponse(
        content={'message': 'User error, check payload data'},
        status_code=status.HTTP_400_BAD_REQUEST
    )


@router.post('/api/task/create')
async def create_cleech_task(data: TaskData):
    is_existed_user = await Users.filter(user_id=data.user['user_id']).first()

    if is_existed_user:
        task_obj, created = await Tasks.get_or_create(
            channel_link=data.channel_link,
            defaults={
                'discription': data.discription,
                'name': data.name,
                #'timer':data.timer,
                'user_id': is_existed_user.id
            }
        )

        if created:
            return JSONResponse(
                content={'data': 'OK'},
                status_code=status.HTTP_201_CREATED
            )

    return JSONResponse(
        content={'data': 'OK'},
        status_code=status.HTTP_200_OK
    )


@router.get('/api/task/list')
async def get_cleech_task_list(user: dict):
    #task_obj = await Users.create(**data.dict())
    #task = await User_Pydantic.from_tortoise_orm(user_obj)

    is_existed_user = await Users.filter(user_id=data.user['user_id']).first()

    if is_existed_user:
        tasks = await Tasks.filter(user_id=is_existed_user.id)

    print(tasks)
    return JSONResponse(
        #content={'task_id': 'hash'},
        status_code=status.HTTP_200_OK
    )


@router.get('/api/task/delete')
async def delete_cleech_task(user: dict, taks_id: int):
    is_existed_user = await Users.filter(user_id=data.user['user_id']).first()

    if is_existed_user:
        task = await Tasks.filter(id=taks_id, user_id=is_existed_user.id).delete()

    return JSONResponse(
        #content={'task_id': 'hash'},
        status_code=status.HTTP_200_OK
    )

# Depends(user)
@router.get('/api/task/edit')
async def edit_cleech_task(user: dict, taks_id: int, data: dict):
    is_existed_user = await Users.filter(user_id=data.user['user_id']).first()

    if is_existed_user:
        task = await Tasks.filter(id=taks_id, user_id=is_existed_user.id)

        await is_created_user.update_from_dict({
            'discription': data.discription,
            'name': data.name,
            'channel_link': data.channel_link,
        }).save()

    return JSONResponse(
        content={'data': 'OK'},
        status_code=status.HTTP_200_OK
    )
