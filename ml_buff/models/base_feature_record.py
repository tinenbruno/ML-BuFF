from ml_buff.models.base_feature_repository import BaseFeatureRepository

class FeatureMeta(type):
    def __init__(cls, name, bases, dct):
        super(FeatureMeta, cls).__init__(name, bases, dct)
        cls._class = cls.__name__

class BaseFeatureRecord(metaclass=FeatureMeta):
    _input_data_values = None

    def __init__(self):
        BaseFeatureRepository().get_or_create(self._class)

    def getModel(self):
        return BaseFeatureRepository().get(self._class)

    def getOrCreateModel(self):
        model = BaseFeatureRepository().get_or_create(self._class)
        return model

    def setInputDataValues(self, input_data_values):
        self._input_data_values = input_data_values

    def calculate(self, input_data):
        return [0]

    def getValue(self, input_data):
        return BaseFeatureRepository().getValue(self._class, input_data)

    def getOrCreateValue(self, input_data):
        try:
            featureValue = self.getValue(input_data)
        except:
            value = self.calculate(input_data)
            BaseFeatureRepository().createValue(self._class, input_data, value)

    def createValue(self, input_data):
        value = self.calculate(input_data)
        BaseFeatureRepository().createValue(self._class, input_data, value)

