from ml_buff.models import feature
from ml_buff.database import session_scope

def test_persistence():
    testfeature = feature.Feature('test')

    with session_scope() as session:
        session.add(testfeature)
        
    with session_scope() as session:
        testfeature = session.query(feature.Feature).order_by(feature.Feature.id.desc()).first()
        session.expunge(testfeature)

    assert testfeature.name == 'test'
    assert testfeature.id != None
