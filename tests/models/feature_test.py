from ml_buff.models.feature import Feature

def test_persistence():
    testfeature = Feature.create(
            name='test')

    assert testfeature.name == 'test'
    assert testfeature.id != None
