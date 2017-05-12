from ml_buff.models.input_data import InputData

class BaseInputDataRepository():
    def get(self, input_data_id):
        return_value = (
            InputData
            .select(InputData)
            .where(InputData.id == input_data_id)
            .get()
        )
        return return_value

    def getAllForDataset(self, dataset_name):
        return (InputData
                .select(InputData)
                .where(InputData.dataset_name == dataset_name)
                )
