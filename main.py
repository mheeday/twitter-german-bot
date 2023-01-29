from typing import Union

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int
    sex: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def return_item(item_id: int, q: Union[Person, None] = None):
    return {"item_id": item_id, "q": q.name}
