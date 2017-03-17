from ml_buff.models import feature, feature_value
from ml_buff.database import session_scope_refresh

def test_persistence():
    testfeature = feature.Feature('test')
    with session_scope_refresh() as session:
      session.add(testfeature)
      session.flush()
      session.refresh(testfeature)
      test_feature_value = feature_value.FeatureValue([10], testfeature)
      session.add(test_feature_value)
      session.flush()
      session.refresh(test_feature_value)

      assert test_feature_value.value[0] == 10
      assert test_feature_value.feature.name == 'test'
      assert test_feature_value.id != None
