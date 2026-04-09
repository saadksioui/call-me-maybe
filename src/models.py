from pydantic import BaseModel
from typing import Dict


class ParameterModel(BaseModel):
    type: str


class FunctionModel(BaseModel):
    name: str
    description: str
    parameters: Dict[str, ParameterModel]
    returns: ParameterModel
