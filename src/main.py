from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"success": True}


@app.options("/")
async def index_options():
    return {"success": True}


@app.post("/cookies")
async def cookies():
    # 1. retrieve any payload, this endpoint gets
    # 2. send data to another server (POST https://postman-echo.com/post)
    ...


@app.options("/cookies")
async def cookies_options():
    # return something here :)
    ...


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
