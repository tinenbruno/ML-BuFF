from ml_buff.models import feature

def test_persistence():
    testfeature = feature.Feature('test')
    
    with session_scope() as session:
    	session.add(testfeature)

    assert testfeature.name == 'test'
    assert testfeature.id != None