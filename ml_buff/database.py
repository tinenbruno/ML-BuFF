from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

DeclarativeBase = declarative_base()

def db_connect():
	return create_engine('sqlite:///:memory:')

def session_connect(db_connect)
	return sessionmaker(bind=db_connect)

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