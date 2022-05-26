from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app =  FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{id}")
def read_item(id:int, q:Union[str, None] = None):
    return {"id": id, "q": q}


@app.put("/items/{id}")
def update_item(id: int, item:Item):
    return {"name": item.name, "id":id}