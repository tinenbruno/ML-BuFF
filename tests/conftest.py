import pytest

from ml_buff import database, settings

@pytest.fixture(scope="session")
def db(request):
	engine = db_connect(**settings.DATABASE)
	db_create(engine)
    return engine