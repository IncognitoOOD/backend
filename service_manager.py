from manager import Manager
from pipeline import Pipeline


class ServiceManager:
    __managers: list

    def __read_all_pipelines(self):
        # read pipelines
        return []

    def __distribute_pipelines(self):
        # distribute pipelines
        pass

    def __find_best_manager(self):
        # find best manager
        return self.__managers[0]

    def add_pipeline_config(self, full_config: dict):
        pipeline = Pipeline(full_config)
        # do some stuff
        return True

    def test_pipeline_config(self, full_config: dict):
        pipeline = Pipeline(full_config)
        # do some stuff
        return True
