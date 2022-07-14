from enum import Enum
from pydantic import BaseModel
from typing import Optional

class LogineUserBody(BaseModel):
    email: str
    name: str
