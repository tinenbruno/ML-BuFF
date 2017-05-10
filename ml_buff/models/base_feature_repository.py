from ml_buff.models.feature import Feature
from ml_buff.models.feature_value import FeatureValue

class BaseFeatureRepository():
    def create(self, classname):
        feature = Feature.create( name = classname )

    def get_or_create(self, classname):
        return Feature.get_or_create( name = classname )

    def get(self, classname):
        return Feature.get( Feature.name == classname )

    def getValue(self, classname, input_data):
        model = (FeatureValue
            .select()
            .join(Feature)
            .where(Feature.name == classname)
            .order_by(FeatureValue.id.desc())
            .get())

        return model

    def createValue(self, classname, input_data, value):
        feature = self.get(classname)
        feature_value = FeatureValue.create(
                value = value,
                feature = feature,
                input_data = input_data)

        return feature_value
