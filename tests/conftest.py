import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/testdatabase')
    if not database_exists(engine.url):
        create_database(engine.url)