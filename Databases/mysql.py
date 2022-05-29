import mysql.connector


class MySQL:
    def __init__(self, config = None):
        self.config = config
        self.db = None
        self.cursor = None
        self.__connect()

    def __connect(self):
        d = {}
        d["host"] = self.config["host"]
        d["port"] = self.config.get("port", 3306)

        d["auth_plugin"] = "mysql_native_password"
        if self.config.get("authentication") == "userpass":
            d["user"] = self.config["username"]
            d["password"] = self.config["password"]
        d["database"] = self.config["database"]
        self.db = mysql.connector.connect(**d)
        self.cursor = self.db.cursor(dictionary=True)
