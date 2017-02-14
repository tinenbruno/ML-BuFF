import sqlalchemy
from datetime import datetime
from ml_buff.database import Base 

class Feature(Base):
  __tablename__ = 'features'

  id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
  name = sqlalchemy.Column(sqlalchemy.String)
  created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
  updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

  def __init__(self, name):
    self.name = name