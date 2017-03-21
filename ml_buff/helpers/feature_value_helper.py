from ml_buff.models.base_feature_record import BaseFeatureRecord
from ml_buff.models.base_input_data_repository import BaseInputDataRepository
from ml_buff.database import session_scope

class FeatureValueHelper():
	def createAll(self, input_data_id_list):
		for input_data_id in input_data_id_list:
			self.createAllForInput(input_data_id)

	def createAllForInput(self, input_data_id):
		subclasses = BaseFeatureRecord.__subclasses__()
		with session_scope() as session:
			input_data = BaseInputDataRepository(session, input_data_id)
		for subclass in subclasses:
			feature = subclass()
			feature.getOrCreateValue(input_data)

	def forceUpdateForInput(self, input_data_id):
		subclasses = BaseFeatureRecord.__subclasses__()
		with session_scope() as session:
			input_data = BaseInputDataRepository(session, input_data_id)
		for subclass in subclasses:
			feature = subclass()
			feature.createValue(input_data)
