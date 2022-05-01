class Pipeline:
    __config: dict
    __extractor: Extractor
    __transformers: list
    __loader: Loader

    def __init__(self, config: dict):
        self.__config = config

    def generate_unique_id(self):
        # generate a random unique string
        return "Unique ID"

    def get_unique_id(self):
        return self.__config['unique_id']

    def should_run(self):
        return self.__config['should_run']

    def run(self):
        # run pipeline
        pass

    def test_pipeline_config(self, full_config: dict):
        # test pipeline
        return True
