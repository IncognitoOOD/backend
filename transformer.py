from data_capsule import DataCapsule


class Transformer:
    config: dict

    def __init__(self, config: dict):
        self.config = config

    def __rename(self, dc: DataCapsule):
        # do some stuff
        return dc

    def __concat(self, dc: DataCapsule):
        # do some stuff
        return dc

    def __api_call(self, dc: DataCapsule):
        # do some stuff
        return dc

    def run(self, dc_list: list):
        # do some stuff
        return dc_list
