import redis
import json

class RedisManager:
    def __init__(self) -> None:
        self.r = redis.Redis(host='redis', port=6379, db=0)
    
    def key_exists(self, id):
        return self.r.exists(id)
    
    def load_state(self, id: str):
        return json.loads(self.r.get(id).decode())

    def save_state(self, id: str, state: dict):
        self.r.set(id, json.dumps(state))
    
if __name__ == "__main__":
    r = RedisManager()
    print(r.key_exists("1"))
    r.save_state("1", "ok")
    print(r.load_state("1") == "ok")
