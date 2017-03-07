from feature import Feature
from feature_value import FeatureValue

class BaseFeatureRepository():
	def create(self, session, classname):
		feature = Feature(classname)
		session.add(self.feature)

	def get(self, session, classname):
		return session.query(Feature).filter(Feature.name == classname).one_or_none()

	def getValue(self, session, classname):
        model = session.query(Feature).options(subqueryload(Feature.feature_values)).filter(Feature.name == classname).order_by(FeatureValue.created_at).first()
        return model.feature_values[0]