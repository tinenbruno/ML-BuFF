import sqlachemy
from datetime import datetime
from ml_buff.database import DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB

class Result(DeclarativeBase):
    __tablename__ = 'result'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    metadata = sqlalchemy.Column(JSONB)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default = datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default = datetime.now)
