import pytest
from ml_buff.database_helper import create_tables, drop_tables

@pytest.fixture(scope="session", autouse=True)
def conf_db(request):
    create_tables()

    def clear():
        drop_tables()
    request.addfinalizer(clear)

