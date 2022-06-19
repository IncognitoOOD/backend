import pymongo

class MongoDB:
    def __init__(self, config):
        self.config = config
        d = {
            "host":       self.mongo_config["host"],
            "port":       self.mongo_config["port"],
            "username":   self.mongo_config["username"],
            "password":   self.mongo_config["password"],
            "database":   self.mongo_config["database"],
            "collection": self.mongo_config["collection"]
        }
        self.client = pymongo.MongoClient(**d)
        self.mydb = self.client[d["database"]]
        self.collection = self.mydb[d["collection"]]

