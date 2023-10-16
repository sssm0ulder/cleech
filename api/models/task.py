from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

from .user import Users


class Tasks(models.Model):
    id = fields.IntField(pk=True)
    channel_link = fields.CharField(max_length=50, unique=True)
    discription = fields.CharField(max_length=256, null=True)  # for TG
    name = fields.CharField(max_length=50, null=True)

    user = fields.ForeignKeyField('models.Users', related_name='tasks')
    #timer = fields.DatetimeField(auto_now_add=True)
    #is_active = fields.BooleanField(default=True)
    #avatar = fields.CharField(max_length=50, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ['created_at', 'modified_at'] 


Task_Pydantic = pydantic_model_creator(Tasks, name='Task')
TaskIn_Pydantic = pydantic_model_creator(Tasks, name='TaskIn', exclude_readonly=True)
