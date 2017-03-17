from ml_buff.models import input_data
from ml_buff.database import session_scope

def test_persistence():
    test_input_data = input_data.InputData(1234,  'datasetTest')

    with session_scope() as session:
        session.add(test_input_data)
        
    with session_scope() as session:
        test_input_data = session.query(input_data.InputData).first()
        session.expunge(test_input_data)

    assert test_input_data.external_id == 1234
    assert test_input_data.dataset_name == 'datasetTest'
    assert test_input_data.id != None
