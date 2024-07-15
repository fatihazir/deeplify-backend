# Deeplify Backend

## Introduction

Welcome to the Deeplify Backend project of Fatih HAZIR. This project is a FastAPI-based backend service designed to handle image classification tasks. It features robust exception handling including end-point check, file type check, a JSON-based fixed response structure, and can be easily extended to include token-based authentication for secure access. The backend is structured to provide clear and consistent responses, ensuring a smooth integration with frontend applications.

## Setup (Without docker, dockerized version below)

1. **Create a virtual environment:**
   ```bash
   python -m venv env

2. **Activate the virtual environment for macOS and Linux:**
   ```bash
   source env/bin/activate

3. **Activate the virtual environment for Windows:**
   ```bash
   env\Scripts\activate

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   or
   pip3 install -r requirements.txt
   or
   python3 -m pip install -r requirements.txt

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload

   After running, it should look like this   

5. **Endpoints:**
   POST /api/v1/classify-image: Accepts an image file and returns a classification label.


## Setup (With docker)
- Make sure docker is running

1. **Build the docker image:**
   ```bash
   docker build -t deeplify-backend .

2. **run the container:**
   ```bash
   docker run -d -p 8000:8000 deeplify-backend

3. **Verify the Setup:**
   After running the Docker container, you can verify the setup by accessing the FastAPI application at http://localhost:8000.


4. **Endpoints:**
   POST /api/v1/classify-image: Accepts an image file and returns related response.


## Testing

1. **Install `pytest` and `httpx`:**
   ```bash
   pip install pytest httpx

2. **Run the tests:**
   ```bash
   pytest

   