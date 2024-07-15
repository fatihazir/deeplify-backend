import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_classify_image_success():
    # Simulate an image upload
    with open("tests/elmır.jpg", "rb") as image:
        response = client.post(
            "/api/v1/classify-image",
            files={"file": image}
        )
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["success"] == True
    assert json_response["message"] == "Image classified successfully"
    assert json_response["data"]["file_name"] == "elmır.jpg"
    assert "image_classification_label" in json_response["data"]

def test_classify_image_no_file():
    response = client.post("/api/v1/classify-image")
    assert response.status_code == 422  # Validation error for missing file
    json_response = response.json()
    assert json_response["success"] == False
    assert "Validation Error" in json_response["message"]
