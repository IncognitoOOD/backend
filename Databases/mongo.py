import pymongo

class MongoDB:
    def __init__(self, config):
        self.config = config
        d = {
            "host":       self.config["host"],
            "port":       self.config["port"],
            "username":   self.config["username"],
            "password":   self.config["password"],
            "database":   self.config["database"],
            "collection": self.config["collection"]
        }
        self.client = pymongo.MongoClient(**d)
        self.mydb = self.client[d["database"]]
        self.collection = self.mydb[d["collection"]]

