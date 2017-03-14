import pytest

from ml_buff import database, settings

@pytest.fixture(scope="session", autouse=True)
def db(request):
	engine = database.db_connect(settings.DATABASE)
	database.db_drop(engine)
	database.db_create(engine)
	return engine
