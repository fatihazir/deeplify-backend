from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.schemas.responses import ErrorResult
from app.schemas.image_data_response import ImageClassificationResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def custom_request_validation_exception_handler(request: Request, exc: RequestValidationError):
    error_response = ErrorResult(message="Validation Error: " + ", ".join([e["msg"] for e in exc.errors()]))
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ImageClassificationResponse(
            success=error_response.success,
            message=error_response.message
        ).model_dump()
    )

async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        error_response = ErrorResult(message="Endpoint not found")
        return JSONResponse(
            status_code=exc.status_code,
            content=ImageClassificationResponse(
                success=error_response.success,
                message=error_response.message
            ).model_dump()
        )
    else:
        error_response = ErrorResult(message=exc.detail)
        return JSONResponse(
            status_code=exc.status_code,
            content=ImageClassificationResponse(
                success=error_response.success,
                message=error_response.message
            ).model_dump()
        )