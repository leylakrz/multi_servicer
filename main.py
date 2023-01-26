from fastapi import FastAPI

from _1 import Command as Command1
from _2 import Command as Command2
from schemas import FirstSchema, SecondSchema

app = FastAPI()


@app.post("/first/")
async def root(body: FirstSchema):
    return {"result": Command1(body.provider).run(body.service, body.arg)}


@app.post("/second/")
async def root(body: SecondSchema):
    return {"result": Command2().run(body.service, body.arg)}

