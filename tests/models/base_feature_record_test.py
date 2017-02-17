from ml_buff.models import base_feature_record, feature
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

class TestFeature(base_feature_record.BaseFeatureRecord):
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        feature.Base.metadata.create_all(self.engine)
        self.feature = feature.Feature(self._class)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session.add(self.feature)
        self.session.commit()

def test_classname():
    test_feature = TestFeature()
    assert test_feature._class == 'TestFeature'

def test_getModel():
    test_feature = TestFeature()
    result = test_feature.getModel()
    assert result.name == 'TestFeature'