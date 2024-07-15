from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from random import choice
from app.schemas.image_data_response import ImageClassificationResponse, ImageClassificationData, create_error_response, create_success_response
from app.dependencies import verify_token

router = APIRouter()

@router.post("/classify-image", response_model=ImageClassificationResponse
             #, dependencies=[Depends(verify_token)]
             )
async def classify_image(file: UploadFile = File(...)):
    ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/jpg"]
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        return create_error_response("Invalid file type. Only image files are allowed.")
     
    try:
        random_classification = choice(["OK", "NOK"])
        file_name = file.filename
        file_size_in_bytes = file.size

        data = ImageClassificationData(
            image_classification_label=random_classification,
            file_name=file_name,
            file_size_in_bytes=file_size_in_bytes
        )

        return create_success_response(data, "Image classified successfully")
    
    except HTTPException as e:
        return create_error_response(str(e))
    
    except Exception as e:
        return create_error_response(str(e))
     
    
    