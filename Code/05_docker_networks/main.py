from fastmcp import FastMCP ## Dependencia no instalada
import httpx ## Dependencia no instalada
from starlette.responses import JSONResponse

## Instanciamos el servidor de FastMCP
app = FastMCP(name="FastMCP-Server")

## Creamos una ruta personalizada para verificar el estado del servidor
@app.custom_route(
    path="/status",
    methods=["GET"],
    name="server_status",
)
async def status(request)-> JSONResponse:
    data = {
        "service": "FastMCP Server",
        "status": "running",
    }
    return JSONResponse(content=data)

## Creamos una herramienta personalizada que devuelve el texto ingresado
@app.tool(
    name="echo_tool",
    description="A tool that echoes the input text."
)
async def echo_tool(input_text: str) -> str:
    return f"Echo: {input_text}"

## Montamos un servidor MCP basando en una API FastAPI desplegada en otra instancia
## API FastAPI desplegada en: http://18.217.229.38/
openapi_cliente = httpx.AsyncClient(base_url="http://18.217.229.38/") 
openapi_cliente_spec = httpx.get("http://18.217.229.38/openapi.json").json()

## Creamos la instancia del servidor FastMCP basado en la API FastAPI
app_2 = FastMCP.from_openapi(
    openapi_spec=openapi_cliente_spec,
    client=openapi_cliente,
    name="FastMCP-Client-FastAPI",
)

## Montamos la segunda aplicación en la ruta /client-api
app.mount(prefix="client-api", server=app_2)

## Ejecutamos el servidor FastMCP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,transport="http")
    
## Ejecución de terminal con comandos docker:

## Paso A). docker-compose up -d
## Paso B). docker-compose ps ## Para ver los contenedores en ejecución

