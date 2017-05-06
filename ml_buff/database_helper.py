from contextlib import contextmanager
from . import settings
from peewee import *
from ml_buff.models.input_data import InputData
from ml_buff.models.feature import Feature
from ml_buff.models.feature_value import FeatureValue
from ml_buff.models.base_model import database

def create_tables():
    database.connect()
    database.create_table(InputData, safe=True)
    database.create_table(Feature, safe=True)
    database.create_tables([Feature, FeatureValue], safe=True)

def get_tables():
    database.get_tables()

def get_database():
    return self.database

def drop_tables():
    database.drop_tables([InputData, Feature, FeatureValue], safe=True)
