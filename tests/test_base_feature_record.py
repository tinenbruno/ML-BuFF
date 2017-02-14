from ml_buff.models import base_feature_record

class TestFeature(base_feature_record.BaseFeatureRecord):
  pass

def test_classname():
    test_feature = TestFeature()
    assert test_feature._class == 'TestFeature'