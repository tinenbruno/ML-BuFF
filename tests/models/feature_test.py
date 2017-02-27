from ml_buff.models import feature

def test_persistence(session):
    testfeature = feature.Feature('test')
    session.add(testfeature)
    session.commit()
    assert testfeature.name == 'test'
    assert testfeature.id != None