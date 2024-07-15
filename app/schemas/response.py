from typing import Any, Optional
from pydantic import BaseModel

class Result(BaseModel):
    success: bool
    message: Optional[str] = None

class DataResult(Result):
    data: Optional[Any] = None