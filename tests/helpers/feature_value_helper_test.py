from ml_buff.models import feature, feature_value, input_data, base_feature_record
from ml_buff.models.input_data import InputData
from ml_buff.models.base_input_data_repository import BaseInputDataRepository
from ml_buff.helpers.feature_value_helper import FeatureValueHelper

class TestFeature1(base_feature_record.BaseFeatureRecord):
    def calculate(self, input_data):
        return [1]
class TestFeature2(base_feature_record.BaseFeatureRecord):
    def calculate(self, input_data):
        return [2]
class TestFeatureCalculate(base_feature_record.BaseFeatureRecord):
    def calculate(self, input_data):
        return self._input_data_values

def test_createAll():
    test_input_data = (input_data.InputData.create(external_id = 1, dataset_name = 'createAll'), input_data.InputData.create(external_id = 2, dataset_name = 'createAll'))

    input_data_list = {}
    for test_input_datum in test_input_data:
        input_data_list[test_input_datum.id] = [1, 2, 3]

    FeatureValueHelper.createAll(input_data_list)

    print(input_data.InputData.get())
    for test_input_datum in test_input_data:
        value1 = TestFeature1().getValue(test_input_datum)
        value2 = TestFeature2().getValue(test_input_datum)

        assert value1.value == [1]
        assert value2.value == [2]

def test_forceUpdateForInput():
    test_input_data = (input_data.InputData.create(external_id = 1, dataset_name = 'createAll'), input_data.InputData.create(external_id = 2, dataset_name = 'createAll'))

    input_data_list = {}
    for test_input_datum in test_input_data:
        input_data_list[test_input_datum.id] = [1, 2, 3]

        FeatureValueHelper.createAll(input_data_list)

    for test_input_datum in test_input_data:
        value = TestFeatureCalculate().getValue(test_input_datum)

        assert value.value == [1,2,3]

    FeatureValueHelper.forceUpdateForInput(test_input_data[0].id, [1])

    value = TestFeatureCalculate().getValue(test_input_data[0])
    assert value.value == [1]
