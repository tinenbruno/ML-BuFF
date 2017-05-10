from ml_buff.models import base_feature_record, feature, feature_value, input_data, base_feature_repository

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
    input_data_test = input_data.InputData.create(
            external_id = 1234,
            dataset_name = 'datasetTest')

    feature_value_first = feature_value.FeatureValue.create(
            value = [9],
            feature = feature,
            input_data = input_data_test)

    assert test_feature.getValue(input_data_test) != None

    feature_value_second = feature_value.FeatureValue.create(
            value = [10],
            feature = feature,
            input_data = input_data_test)

    result = test_feature.getValue(input_data_test)
    assert result.value == [10.0]
