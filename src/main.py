from urllib import response
from fastapi import FastAPI, HTTPException
import uvicorn
from logging_config import logger
import requests


app = FastAPI()


@app.get("/")
async def index():
    logger.info("INDEX ENDPOINT TRIGGERED")
    return {"success": True}


@app.options("/")
async def index_options():
    return {"success": True}


@app.post("/cookies")
async def cookies(payload: dict):
    response = requests.post("https://postman-echo.com/post", json=payload)
    if response.status_code == 200:
        logger.info(f"Received payload data: {payload}")
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code,
                            detail="Request failed")


@app.options("/cookies")
async def cookies_options():
    response = {
        "Allow": "GET, POST",
        "Access-Control-Allow-Origin": "*",
    }
    return response


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
