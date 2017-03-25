from ml_buff.database import session_scope
from ml_buff.models import feature, feature_value, input_data, base_feature_record
from ml_buff.helpers.feature_value_helper import FeatureValueHelper

class TestFeature1(base_feature_record.BaseFeatureRecord): 
    def calculate(self, input_data):
        return [1]
class TestFeature2(base_feature_record.BaseFeatureRecord):
    def calculate(self, input_data):
        return [2]

def test_createAll():
    test_input_data = (input_data.InputData(1, 'createAll'), input_data.InputData(2, 'createAll'))
    with session_scope() as session:
        for test_input_datum in test_input_data:
            session.add(test_input_datum)

    with session_scope() as session:
        test_input_data = session.query(input_data.InputData).filter(input_data.InputData.dataset_name == 'createAll').all()
        for test_input_datum in test_input_data:
            session.expunge(test_input_datum)

    input_data_ids = [o.id for o in test_input_data]
    FeatureValueHelper.createAll(input_data_ids)

    for test_input_datum in test_input_data:
        value1 = TestFeature1().getValue(test_input_datum)
        value2 = TestFeature2().getValue(test_input_datum)
        
        assert value1.value == [1]
        assert value2.value == [2]
