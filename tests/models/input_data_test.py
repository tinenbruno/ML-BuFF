from ml_buff.models.input_data import InputData
from ml_buff.database import session_scope

def test_persistence():
    test_input_data = InputData(1234,  'datasetTest')

    with session_scope() as session:
        session.add(test_input_data)

    with session_scope() as session:
        test_input_data = session.query(InputData).filter(InputData.external_id == 1234, InputData.dataset_name == 'datasetTest').first()
        session.expunge(test_input_data)

    assert test_input_data.external_id == 1234
    assert test_input_data.dataset_name == 'datasetTest'
    assert test_input_data.id != None
