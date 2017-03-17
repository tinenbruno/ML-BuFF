from ml_buff.models import base_feature_record, feature, feature_value
from ml_buff.database import session_scope

class TestFeature(base_feature_record.BaseFeatureRecord): pass

def test_classname():
    test_feature = TestFeature()
    assert test_feature._class == 'TestFeature'

def test_getModel():
    test_feature = TestFeature()
    result = test_feature.getModel()
    assert result.name == 'TestFeature'

def test_getValue():
    test_feature = TestFeature()
    feature = test_feature.getModel()

    assert len(feature.feature_values) == 0

    feature_value_first = feature_value.FeatureValue([9], feature)
    with session_scope() as session:
        session.add(feature_value_first)

    feature = test_feature.getModel()
    assert feature.feature_values != None

    feature_value_second = feature_value.FeatureValue([10], feature)
    
    with session_scope() as session:
        session.add(feature_value_second)

    result = test_feature.getValue()
    assert result.value == [10.0]
