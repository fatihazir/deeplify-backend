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

def test_classify_image_invalid_file_type():
    # Simulate an invalid file type upload
    with open("tests/fakefile.txt", "wb") as f:
        f.write(b"This is a test.")
    with open("tests/fakefile.txt", "rb") as file:
        response = client.post(
            "/api/v1/classify-image",
            files={"file": file}
        )
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["success"] == False
    assert json_response["message"] == "Invalid file type. Only image files are allowed."

def test_classify_multiple_files():
    # Simulate multiple file upload
    with open("tests/elmır.jpg", "rb") as image, open("tests/fakefile.txt", "rb") as fake_file:
        response = client.post(
            "/api/v1/classify-image",
            files={"file1": ("elmır.jpg", image), "file2": ("fakefile.txt", fake_file)}
        )
    json_response = response.json()
    assert json_response["success"] == False