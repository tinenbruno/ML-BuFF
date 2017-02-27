import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database, drop_database
from ml_buff.models import feature, feature_value
from ml_buff import database

TEST_DATABASE = 'postgresql://postgres:postgres@localhost:5432/testdatabase'

@pytest.fixture(scope="session")
def db(request):
    engine = create_engine(TEST_DATABASE)
    if not database_exists(engine.url):
        create_database(engine.url)
    database.Base.metadata.create_all(engine)

    return engine

@pytest.fixture(scope="function")
def session(db):
    _session = sessionmaker(bind=db)
    return _session()