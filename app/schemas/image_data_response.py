
from pydantic import BaseModel
from app.schemas.responses import DataResult

class ImageClassificationData(BaseModel):
    image_classification_label: str
    file_name: str
    file_size_in_bytes: int

class ImageClassificationResponse(DataResult[ImageClassificationData]):
    pass


def create_success_response(data: ImageClassificationData, message: str) -> ImageClassificationResponse:
    return ImageClassificationResponse(
        success=True,
        message=message,
        data=data
    )

def create_error_response(message: str) -> ImageClassificationResponse:
    return ImageClassificationResponse(
        success=False,
        message=message
    )