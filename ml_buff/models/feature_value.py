import sqlalchemy
from datetime import datetime
from ml_buff.database import DeclarativeBase 
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

class FeatureValue(DeclarativeBase):
  __tablename__ = 'feature_values'

  id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
  value = sqlalchemy.Column(ARRAY(sqlalchemy.Float))
  feature_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('features.id'))
  feature = relationship("Feature")
  input_data_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('inputs.id'))
  input_data = relationship("InputData")
  created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
  updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)


  def __init__(self, value, feature):
    self.value = value
    self.feature = feature
