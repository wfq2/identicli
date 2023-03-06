from typing import List

from pydantic import BaseModel


class NWZone(BaseModel):
    id: str
    name: str
    state: str
    timeZone: List[str]
    type: str


class NWForecast(BaseModel):
    id: str
    type: str
