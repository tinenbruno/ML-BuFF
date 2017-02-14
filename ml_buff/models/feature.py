import sqlalchemy
class Feature(Base):
  __tablename__ = 'features'

  id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
  name = sqlalchemy.Column(sqlalchemy.Name)
  created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
  updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)