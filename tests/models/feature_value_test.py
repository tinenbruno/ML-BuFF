from ml_buff.models import feature, feature_value

def test_persistence():
    testfeature = feature.Feature('test')
    with session_scope() as session:
    	session.add(testfeature)

    test_feature_value = feature_value.FeatureValue([10], testfeature)
    with session_scope() as session:
    	session.add(test_feature_value)

    assert test_feature_value.value[0] == 10
    assert test_feature_value.feature.name == 'test'
    assert test_feature_value.id != None
