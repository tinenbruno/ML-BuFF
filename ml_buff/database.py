from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from contextlib import contextmanager

import settings
from models import feature, feature_value

DeclarativeBase = declarative_base()

def db_connect(database):
	return create_engine(URL(database))

def db_create(engine):
	if not database_exists(engine.url):
        create_database(engine.url)
    database.Base.metadata.create_all(engine)

def session_connect(db_connect)
	return sessionmaker(bind=db_connect)

Session = session_connect(db_connect(**settings.DATABASE))

@contextmanager
def session_scope():
	session = Session()
	try:
		yield session
		session.commit()
	except Exception as e:
		session.rollback()
		raise
	finally:
		session.close()