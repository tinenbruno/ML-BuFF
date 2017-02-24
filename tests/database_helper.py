from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from ml_buff.models import feature
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql://postgres:postgres@localhost:5432/testdatabase')
if not database_exists(engine.url):
    create_database(engine.url)
feature.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)