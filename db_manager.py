from enum import unique
import json
import pymongo

class MongoManager:
    def __init__(self):
        self.mongo_config = json.loads(open("db_configs/mongo_config.json", "r").read())
        d = {
            "host":       self.mongo_config["host"],
            "port":       self.mongo_config["port"],
            "username":   self.mongo_config["username"],
            "password":   self.mongo_config["password"],
            "database":   self.mongo_config["database"],
            "collection": self.mongo_config["collection"],
            "replica_set": self.mongo_config["replica_set"]
        }
        # self.connection = ReplicaSetConnection("mongodb://{}:{}/".format(d["host"], str(d["port"])), str(d["replica_set"]))
        # print(self.connection)
        # hosts = ["localhost:27017", "localhost:27018", "localhost:27019"]
        # self.client = pymongo.MongoClient(hosts, replicaSet=d["replica_set"])
        # hosts = ["mongodb://{}:{}/".format(h, str(d["port"])) for h in d["host"]]
        self.client = pymongo.MongoClient(d["host"], replicaSet=d["replica_set"])
        print(self.client)
        self.mydb = self.client[d["database"]]
        self.configs = self.mydb[d["collection"]]

    def select(self):
        result = self.configs.find()
        return [item for item in result]

    def get_all_keys(self):
        result = self.configs.find()
        return [item["unique_id"] for item in result if "unique_id" in item]


    def insert(self, document: dict):
        self.configs.insert_one(document)

    def search_by_condition(self, conditions: dict):
        result = self.configs.find(conditions)
        return [item for item in result]

    def disable(self, conditions: dict):
        self.configs.update_one(conditions, {"$set": {"disabled": True}})

    def enable(self, conditions: dict):
        self.configs.update_one(conditions, {"$set": {"disabled": False}})


if __name__ == "__main__":
    db = MongoManager()
    # print(db.select())
    # db.insert({"name": "Till", "family": "Lindemann"})
    # db.insert({"name": "reznov", "nickname": "hero wolf of berlin"})

    print(db.select())
    # db.disable({"name": "reznov"})
    # print(db.select())
    # # print(db.search_by_condition({"name": "reznov"}))
    # db.enable({"name": "reznov"})
    # print(db.select())


