from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"success": True}


@app.options("/")
async def index_options():
    ...


@app.post("/cookies")
async def cookies():
    ...


@app.options("/cookies")
async def cookies_options():
    ...


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
