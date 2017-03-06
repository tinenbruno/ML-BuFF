from . import feature

class BaseFeatureRepository():
	def create(self, session, classname):
		feature = feature.Feature(classname)
		session.add(self.feature)

	def get(self, session, classname):
		return session.query(feature.Feature).filter(feature.Feature.name == classname).one_or_none()

	def getValue(self, session, classname):
        model = self.get(session, classname)
        return model.feature_values[0]