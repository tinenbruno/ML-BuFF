from datetime import datetime
from ml_buff.models.base_model import BaseModel
from ml_buff.models.feature import Feature
from ml_buff.models.input_data import InputData
from playhouse.postgres_ext import *

class FeatureValue(BaseModel):
  value = ArrayField(DoubleField)
  feature = ForeignKeyField(Feature)
  input_data = ForeignKeyField(InputData)
  created_at = DateTimeField(default = datetime.now)
  updated_at = DateTimeField(default = datetime.now)
