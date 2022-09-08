from fastapi import FastAPI, status

app = FastAPI()


@app.get('/')
async def root():
    response = {"name": "Joe Doe", "profession": "Software Engineer"}
    return response


@app.get("/checks", status_code=status.HTTP_200_OK)
async def healthcheck():
    response = {"statusCode": 200, "description": "Success"}
    return response
