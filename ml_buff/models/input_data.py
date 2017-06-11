from datetime import datetime
from peewee import *
from ml_buff.models.base_model import BaseModel

class InputData(BaseModel):
    external_id = IntegerField()
    dataset_name = CharField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField
