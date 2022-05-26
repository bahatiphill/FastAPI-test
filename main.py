from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet =  "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_db_items = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def read_item_2(skip: int=0, limit: int =10):
    return fake_db_items[skip : limit+skip]

@app.get("/items/{item_id}")
async def read_item(item_id: int)-> dict:
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message":"Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message":"LeCNN all the images"}

    return {"model_name": model_name, "message":"Have some residuals"}
