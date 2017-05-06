from datetime import datetime
from peewee import *
from ml_buff.models.base_model import BaseModel

class Feature(BaseModel):
  name = CharField(unique=True)
  created_at = DateTimeField(default=datetime.now)
  updated_at = DateTimeField(default=datetime.now)
