from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import Model

database = PostgresqlExtDatabase(
    'ml_buff',
    user='postgres',
    password='postgres',
    host='localhost',
    register_hstore=False,
)

class BaseModel(Model):
    class Meta:
        database = database
