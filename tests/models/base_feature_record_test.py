from ml_buff.models import base_feature_record, feature, feature_value, input_data
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
    input_data_test = input_data.InputData(1234, 'datasetTest')

    feature_value_first = feature_value.FeatureValue([9], feature, input_data_test)
    with session_scope() as session:
        session.add(feature_value_first)

    feature = test_feature.getModel()
    assert feature.feature_values != None

    feature_value_second = feature_value.FeatureValue([10], feature, input_data_test)

    with session_scope() as session:
        session.add(feature_value_second)

    with session_scope() as session:
        input_data_test = session.query(input_data.InputData).order_by(-input_data.InputData.id).first()
        session.expunge(input_data_test)

    result = test_feature.getValue(input_data_test)
    assert result.value == [10.0]
