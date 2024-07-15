from pydantic import BaseModel
from typing import Optional
from app.schemas.response import DataResult

class ImageClassificationData(BaseModel):
    image_classification_label: str
    file_name:str
    file_size_in_bytes:int

    
class ImageClassificationResponse(DataResult):
    data: Optional[ImageClassificationData] = None