from ml_buff.models import feature, feature_value, input_data

def test_persistence():
    testfeature = feature.Feature.create(
            name = 'test_persistence')
    test_input_data = input_data.InputData.create(
            external_id = 1234,
            dataset_name = 'datasetTest')

    test_feature_value = feature_value.FeatureValue.create(
            value = [10],
            feature = testfeature,
            input_data = test_input_data)

    assert test_feature_value.value[0] == 10
    assert test_feature_value.feature.name == 'test_persistence'
    assert test_feature_value.id != None
