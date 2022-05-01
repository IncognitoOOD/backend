from pipeline import Pipeline


class Manager:
    __pipelines: list

    def __save_log(self, log: dict):
        # save log
        pass

    def run(self):
        # run manager
        pass

    def get_number_of_pipelines(self):
        return 0

    def add_pipeline(self, full_config: dict):
        # add pipeline
        pass

    def test_pipeline_config(self, full_config: dict):
        pipeline = Pipeline(full_config)
        # do some stuff
        pass
