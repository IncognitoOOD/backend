import threading
from pipeline import Pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, FastAPI
from db_manager import MongoManager
import uvicorn


class Manager:
    def __init__(self):
        self.__pipelines = []
        self.db = MongoManager()

    def run(self):
        # run manager
        while True:
            for pipeline in self.__pipelines:
                if pipeline.should_run():
                    pipeline.run()
                    self.db.disable(pipeline.get_config())

    def add_pipeline(self, full_config: dict):
        # add pipeline
        p = Pipeline(full_config)
        self.__pipelines.append(p)
        manager.db.insert(p.get_config())
        return p.get_unique_id()

    def test_pipeline_config(self, full_config: dict):
        return Pipeline.test_pipeline_config(full_config)


manager = Manager()
t = threading.Thread(target=manager.run)
t.start()

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/add_pipeline_config")
async def add_pipeline_config(request: Request):
    config = await request.json()
    test_result = manager.test_pipeline_config(config)
    if not test_result[0]:
        return {"status": "not_ok", "error_messages": test_result[1]}
    unique_id = manager.add_pipeline(config)
    return {"status": "ok", "unique_id": unique_id}


@app.get("/retrieve_key/{unique_id}")
def retrieve(request: Request, unique_id):
    result = manager.db.search_by_condition({"unique_id": unique_id})
    result[0].pop("_id")
    return result[0]


if __name__ == "__main__":
    uvicorn.run("manager:app", host="127.0.0.1", port=8000, reload=False)
