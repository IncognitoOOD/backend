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
        pass_d = {
            "host":       self.config["host"],
            "port":       self.config["port"]
        }
        if "username" in self.config and "password" in self.config:
            pass_d["username"] = self.config["username"]
            pass_d["password"] = self.config["password"]
        self.client = pymongo.MongoClient(**pass_d)
        self.mydb = self.client[d["database"]]
        self.collection = self.mydb[d["collection"]]

