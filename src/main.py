from urllib import response
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from logging_config import logger
import requests


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5000",

    "https://fatalista-https-middleware.onrender.com/cookies",
    "https://fatalista-https-middleware.onrender.com",

    "https://3.75.158.163:8000",
    "https://3.125.183.140:8000",
    "https://35.157.117.28:8000",

    "https://3.75.158.163:8000/cookies",
    "https://3.125.183.140:8000/cookies",
    "https://35.157.117.28:8000/cookies",

    # dragontail
    "https://dragontail.choiceqr.com"

    # fatalis
    "https://fatalistbar.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    logger.info("INDEX ENDPOINT TRIGGERED")
    return {"success": True}


@app.options("/")
async def index_options():
    return {"success": True}


@app.post("/cookies")
async def cookies(request: Request):

    try:
        payload = await request.json()
        logger.info(f"PAYLOAD RECEIVED - {payload}")
    except Exception as ex:
        logger.error(f"!!! ERROR OCCURRED - {ex}")
        raise HTTPException(status_code=422,
                            detail="Bad Payload")


    logger.info("SENDING DATA TO AWS")
    response = requests.post("http://52.23.187.142:5000/post_cookies_fatalist", json=payload)

    aws_status_code = response.status_code
    aws_data = response.json()

    logger.info(f"AWS STATUS CODE - {aws_status_code}; AWS RESPONSE - {aws_data}")

    if response.status_code == 200:
        logger.info(f"SUCCESSFULLY SENT DATA TO AWS")
        return JSONResponse(content=aws_data, headers={"Access-Control-Allow-Origin": "*"})
    else:
        logger.warning("! FAILED SENDING DATA TO AWS")
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
    # uvicorn.run(app=app, host="127.0.0.1", port=8000)
