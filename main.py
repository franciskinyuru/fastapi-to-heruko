from fastapi import FastAPI, status
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    response = {"name": "Joe Doe", "profession": "Software Engineer"}
    return response


@app.get("/checks", status_code=status.HTTP_200_OK)
async def healthcheck():
    response = {"statusCode": 200, "description": "Success"}
    return response


@app.get("/items", status_code=status.HTTP_200_OK)
async def check():
    response = {"Framework": "FastAPI", "Author": "Tiangolo"}
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
