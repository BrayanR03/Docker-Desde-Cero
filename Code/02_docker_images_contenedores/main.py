from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException

from app.app.routers.clientes import clientes_router



app = FastAPI()
app.include_router(clientes_router)

@app.get(path="/",status_code=status.HTTP_200_OK)
async def main():
    return {"message": "Hello, World desde FastAPI!"}