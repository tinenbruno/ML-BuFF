from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

Base = declarative_base()

Engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=Engine)