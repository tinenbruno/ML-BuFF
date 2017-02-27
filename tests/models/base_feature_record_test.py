from ml_buff.models import base_feature_record, feature

class TestFeature(base_feature_record.BaseFeatureRecord):
    def __init__(self, session):
        self.session = session
        if (self.getModel() == None):
            self.feature = feature.Feature(self._class)
            self.session.add(self.feature)
            self.session.commit()

def test_classname(session):
    test_feature = TestFeature(session)
    assert test_feature._class == 'TestFeature'

def test_getModel(session):
    test_feature = TestFeature(session)
    result = test_feature.getModel()
    assert result.name == 'TestFeature'