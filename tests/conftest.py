import pytest

from ml_buff import database, settings

@pytest.fixture(scope="session", autouse=True)
def db(request):
    engine = database.db_connect(settings.DATABASE)
    try:
        database.db_drop(engine)
    except:
        pass
    database.db_create(engine)
    def fin():
        database.db_drop(engine)
    request.addfinalizer(fin)
    return engine
