# GitHub Gist API

## Overview
This project implements a simple HTTP API that  retrieves public GitHub gists for a given user.

## Tech Stack
- Python
- FastAPI
- Pytest
- Docker

## Run Locally

pip install -r requirements.txt  
uvicorn app.main:app --host 0.0.0.0 --port 8080  

## API Endpoint

GET /users/{username}/gists

Example:
http://localhost:8080/users/octocat/gists

## Run Tests

pytest
python -m pytest .\test_api.py
if any error please install the below 
pip install pytest
pip install fastapi httpx
pip install request httpx

## Docker

### Build
cd gist-api
docker build -t gist-api .

### Run
docker run -p 8080:8080 gist-api

## Test Case

Uses GitHub username: octocat

Validates:
- API responds successfully (HTTP 200)
- Response is a list of gists

