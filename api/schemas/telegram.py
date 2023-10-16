from datetime import datetime

from pydantic import BaseModel


class ConditionData(BaseModel):
    user_id: str
    link: str


class TaskData(BaseModel):
    discription: str
    name: str
    channel_link: str
    timer: datetime = None
    user: dict


class TelegramUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    user_id: str
    tg_hash: str
