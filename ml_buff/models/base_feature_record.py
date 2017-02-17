from . import feature
from ml_buff.database import Session

class FeatureMeta(type):
    def __init__(cls, name, bases, dct):
        super(FeatureMeta, cls).__init__(name, bases, dct)
        cls._class = cls.__name__

class BaseFeatureRecord(metaclass=FeatureMeta):
    def __init__(self):
      self.session = Session()
      if (self.getModel() == None):
          self.feature = feature.Feature(self._class)
          self.session.add(self.feature)
          self.session.commit()
          
    def getModel(self):
        return self.session.query(feature.Feature).filter(feature.Feature.name == self._class).one_or_none()