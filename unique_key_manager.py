import threading
from db_manager import MongoManager
import random
from threading import Thread

class UniqueKeyManager:
    def __init__(self):
        self.db = MongoManager()
        self.used_keys = set(self.db.get_all_keys())
        self.num_of_keys = 20
        self.keys = []
        self.watch_keys()

    def watch_keys(self):
        while True:
            if len(self.keys) < self.num_of_keys:
                key = self.__generate_one_key()
                if key not in self.used_keys:
                    self.keys.append(key)
                    self.used_keys.add(key)
            else:
                break

    def __generate_one_key(self):
        x = ""
        for i in range(8):
            x += str(random.randint(0, 9))
        return x

    def get_unique_key(self):
        if len(self.keys) == 0:
            self.watch_keys()
        key = self.keys.pop()
        Thread(target=self.watch_keys).start()
        return key

if __name__ == "__main__":
    um = UniqueKeyManager()
    print(um.get_unique_key())
    print(um.keys)
    print(um.get_unique_key())
    print(um.get_unique_key())
    print(um.get_unique_key())
    print(um.keys)
    