from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from random import choice
from app.schemas.image_data_response import ImageClassificationResponse, ImageClassificationData
from app.schemas.results import SuccessDataResult, ErrorResult
from app.dependencies import verify_token

router = APIRouter()

@router.post("/classify-image", response_model=ImageClassificationResponse
             #, dependencies=[Depends(verify_token)]
             )
async def classify_image(file: UploadFile = File(...)):
    try:
        random_classification = choice(["OK", "NOK"])
        file_name = file.filename
        file_size_in_bytes = file.size

        data = ImageClassificationData(
            image_classification_label=random_classification,
            file_name=file_name,
            file_size_in_bytes=file_size_in_bytes
        )

        success_response = SuccessDataResult(data=data, message="Image classified successfully")

        return ImageClassificationResponse(
            success=success_response.success,
            message=success_response.message,
            data=success_response.data
        )
    
    except HTTPException as e:
        error_response = ErrorResult(message=str(e))
        return ImageClassificationResponse(
            success=error_response.success,
            message=error_response.message
        )
    
    except Exception as e:
        error_response = ErrorResult(message=str(e))
        return ImageClassificationResponse(
            success=error_response.success,
            message=error_response.message
        )
     
    
    