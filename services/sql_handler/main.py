from fastapi import FastAPI

from typing import Optional

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/{sample_id}/{thing}")
async def read_item(sample_id, thing):
    sql_query="SELECT * FROM {thing}"
    return {"sample_id": sample_id, "thing": thing}
