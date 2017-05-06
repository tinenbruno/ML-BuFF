from ml_buff.models.input_data import InputData

def test_persistence():
    test_input_data = InputData.create( external_id=1234,
                                        dataset_name='datasetTest')

    assert test_input_data.external_id == 1234
    assert test_input_data.dataset_name == 'datasetTest'
    assert test_input_data.id != None
