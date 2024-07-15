from typing import Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    success: bool
    message: Optional[str] = None