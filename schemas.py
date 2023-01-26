from pydantic import BaseModel


class SecondSchema(BaseModel):
    service: str
    arg: str


class FirstSchema(SecondSchema):
    provider: str
    service: str
    arg: str
