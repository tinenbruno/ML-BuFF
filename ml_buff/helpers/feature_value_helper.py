from ml_buff.models.base_feature_record import BaseFeatureRecord
from ml_buff.models.base_input_data_repository import BaseInputDataRepository

class FeatureValueHelper():
    @classmethod
    def createAll(self, input_data_list):
        for input_data in input_data_list:
            self.createAllForInput(input_data['input_id'],input_data['values'])

    @classmethod
    def createAllForInput(self, input_data_id, values):
        subclasses = BaseFeatureRecord.__subclasses__()

        for subclass in subclasses:
            input_instance = BaseInputDataRepository().get(input_data_id)
            feature = subclass()
            feature.setInputDataValues(values)
            feature.getOrCreateValue(input_instance)


    @classmethod
    def forceUpdateForInput(self, input_data_id, values):
        subclasses = BaseFeatureRecord.__subclasses__()
        input_data = BaseInputDataRepository().get(input_data_id)
        for subclass in subclasses:
            feature = subclass()
            feature.setInputDataValues(values)
            feature.createValue(input_data)

    @classmethod
    def getAll(self, input_data_ids):
        subclasses = BaseFeatureRecord.__subclasses__()
        return_value = {}
        for subclass in subclasses:
            feature = subclass()
            return_value[feature._class] = feature.getInputDataValues(input_data_ids)

        return return_value
