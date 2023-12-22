from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataInValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_ingestion = DataInValidation(config = data_validation_config)
            data_ingestion.validate_all_files_exists()
        except Exception as e:
            raise e
