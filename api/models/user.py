from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    user_id = fields.CharField(max_length=50, unique=True)  # for TG
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=10, default='user')
    tg_hash = fields.CharField(max_length=256, null=True)
    is_bot = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ['created_at', 'modified_at', 'is_bot', 'category'] # 'tg_hash', 


User_Pydantic = pydantic_model_creator(Users, name='User')
UserIn_Pydantic = pydantic_model_creator(Users, name='UserIn', exclude_readonly=True)
