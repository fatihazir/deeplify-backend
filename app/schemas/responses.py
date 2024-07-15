from typing import Generic, TypeVar, Optional
from app.schemas.base_response import BaseResponse

T = TypeVar("T")

class DataResult(Generic[T], BaseResponse):
    data: Optional[T] = None

class SuccessDataResult(DataResult[T]):
    def __init__(self, data: Optional[T] = None, message: Optional[str] = None):
        super().__init__(success=True, data=data, message=message)

class ErrorResult(BaseResponse):
    def __init__(self, message: Optional[str] = None):
        super().__init__(success=False, message=message)