import threading
from pipeline import Pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, FastAPI


class Manager:
    def __init__(self):
        self.__pipelines = []

    def run(self):
        # run manager
        while True:
            for pipeline in self.__pipelines:
                if pipeline.should_run():
                    pipeline.run()

    def get_number_of_pipelines(self):
        return len(self.__pipelines)

    def add_pipeline(self, full_config: dict):
        # add pipeline
        p = Pipeline(full_config)
        self.__pipelines.append(p)
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
    id = manager.add_pipeline(config)
    return {"status": "ok", "unique_id": id}


@app.post("/test_pipeline_config")
async def test_pipeline_config(request: Request):
    config = await request.json()

    # if state == 0:
    #     d = {
    #         "status": "not_ok",
    #         "error_messages": ["there was a problem in extractor query", "loader table doesn't exist"]
    #     }
    # else:
    #     d = {
    #         "status": "ok"
    #     }
    # state = 1 - state
    return {"status": "ok"}
