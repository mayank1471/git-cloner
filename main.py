from fastapi import FastAPI
from pydantic import BaseModel

import GitUtils

app = FastAPI()


class WebhookRequest(BaseModel):
    source_repository: str
    destination_repository: str

#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.post("/webhook")
async def process_mirroring(webhook_model: WebhookRequest):
    return GitUtils.clone_and_mirror_repository(webhook_model.source_repository, webhook_model.destination_repository)

#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='8000')
