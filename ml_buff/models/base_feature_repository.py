from ml_buff.models.feature import Feature
from ml_buff.models.feature_value import FeatureValue
from sqlalchemy.orm import joinedload 

class BaseFeatureRepository():
    def create(self, session, classname):
        feature = Feature(classname)
        session.add(feature)
        session.expunge(feature)
        return feature

    def get(self, session, classname):
        return_value = (
            session.query(Feature)
            .options(joinedload("feature_values"))
            .filter(Feature.name == classname)
            .one_or_none()
        )
        if return_value is not None:
            session.expunge(return_value)
        return return_value

    def getValue(self, session, classname, input_data):
        model = (
            session.query(FeatureValue)
            .options(joinedload("feature"))
            .filter(
                Feature.name == classname, 
                FeatureValue.input_data_id == input_data.id
            )
            .order_by(FeatureValue.id.desc())
            .first()
        )
        if model is not None:
            session.expunge(model)
        return model

    def createValue(self, session, classname, input_data, value):
        feature = get(self, session, classname)
        feature_value = FeatureValue(value, feature, input_data)
        session.add(feature_value)
        session.expunge(feature_value)
        return feature_value