from ml_buff.models import feature, feature_value, input_data
from ml_buff.database import session_scope_refresh

def test_persistence():
    testfeature = feature.Feature('test')
    test_input_data = input_data.InputData(1234, 'datasetTest')
    with session_scope_refresh() as session:
      session.add(testfeature)
      session.flush()
      session.refresh(testfeature)
      session.add(test_input_data)
      session.flush()
      session.refresh(test_input_data)
      test_feature_value = feature_value.FeatureValue([10], testfeature, test_input_data)
      session.add(test_feature_value)
      session.flush()
      session.refresh(test_feature_value)

      assert test_feature_value.value[0] == 10
      assert test_feature_value.feature.name == 'test'
      assert test_feature_value.id != None
