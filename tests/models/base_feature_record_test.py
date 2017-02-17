from ml_buff.models import base_feature_record, feature
from tests import database_helper

class TestFeature(base_feature_record.BaseFeatureRecord):
    def __init__(self):
        self.session = database_helper.Session()
        if (self.getModel() == None):
            self.feature = feature.Feature(self._class)
            self.session.add(self.feature)
            self.session.commit()

def test_classname():
    test_feature = TestFeature()
    assert test_feature._class == 'TestFeature'

def test_getModel():
    test_feature = TestFeature()
    result = test_feature.getModel()
    assert result.name == 'TestFeature'