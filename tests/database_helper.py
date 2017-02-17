from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from ml_buff.models import feature

engine = create_engine('sqlite:///:memory:')
feature.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)