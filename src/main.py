# индекс для теста
# /cookies (post - get request and send to another url)
#           (options - return {"success": True} )
from fastapi import FastAPI, Query, status


app = FastAPI()


@app.get("/")
async def index():
    return {"success": True}
