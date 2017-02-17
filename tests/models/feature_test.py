from ml_buff.models import feature
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

def test_persistence():
    engine = create_engine('sqlite:///:memory:')
    feature.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    testfeature = feature.Feature('test')
    session.add(testfeature)
    session.commit()
    assert testfeature.name == 'test'
    assert testfeature.id != None