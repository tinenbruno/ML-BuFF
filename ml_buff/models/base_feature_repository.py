from ml_buff.models.feature import Feature
from ml_buff.models.feature_value import FeatureValue
from sqlalchemy.orm import joinedload 

class BaseFeatureRepository():
        def create(self, session, classname):
            feature = Feature(classname)
            session.add(feature)

        def get(self, session, classname):
            return_value = session.query(Feature).options(joinedload("feature_values")).filter(Feature.name == classname).one_or_none()
            if return_value is not None:
                session.expunge(return_value)
            return return_value

        def getValue(self, session, classname):
            model = session.query(FeatureValue).options(joinedload("feature")).filter(Feature.name == classname).order_by(FeatureValue.id.desc()).first()
            if model is not None:
                session.expunge(model)
            return model
