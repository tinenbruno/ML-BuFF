from . import feature, base_feature_repository
from ml_buff.database import Session, session_scope

class FeatureMeta(type):
    def __init__(cls, name, bases, dct):
        super(FeatureMeta, cls).__init__(name, bases, dct)
        cls._class = cls.__name__

class BaseFeatureRecord(metaclass=FeatureMeta):
    def __init__(self):
      if (self.getModel() == None):
          with session_scope() as session:
            BaseFeatureRepository().create(session, self._class)

    def getModel(self):
        with session_scope() as session:
            return BaseFeatureRepository().getModel(session, self._class)

    def getValue(self):
        with session_scope() as session:
            return BaseFeatureRepository().getValue(session, self._class)