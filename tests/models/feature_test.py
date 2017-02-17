from ml_buff.models import feature
from tests import database_helper

def test_persistence():
    session = database_helper.Session()

    testfeature = feature.Feature('test')
    session.add(testfeature)
    session.commit()
    assert testfeature.name == 'test'
    assert testfeature.id != None