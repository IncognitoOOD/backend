from pipeline import Pipeline


class Manager:
    __pipelines: list

    def run(self):
        # run manager
        while True:
            for pipeline in self.__pipelines:
                if pipeline.should_run():
                    pipeline.run()

    def get_number_of_pipelines(self):
        return len(self.__pipelines)

    def add_pipeline(self, full_config: dict):
        # add pipeline
        self.__pipelines.append(Pipeline(full_config))

    def test_pipeline_config(self, full_config: dict):
        return pipeline.test_pipeline_config(full_config)
