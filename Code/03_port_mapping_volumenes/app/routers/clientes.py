from fastapi import APIRouter
from fastapi import status 
from fastapi import HTTPException

clientes_router = APIRouter(
    tags={"Clientes"},
    prefix="/clientes",
    responses={404: {"message": "No encontrado"}},
)


@clientes_router.get(path="/", status_code=status.HTTP_200_OK)
async def get_clientes():
    return {"message": "Lista de clientes"}