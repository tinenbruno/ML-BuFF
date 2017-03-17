from ml_buff.models.base_feature_repository import BaseFeatureRepository
from ml_buff.database import session_scope

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
            return BaseFeatureRepository().get(session, self._class)

    def getValue(self):
        with session_scope() as session:
            return BaseFeatureRepository().getValue(session, self._class)
