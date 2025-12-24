from fastmcp import FastMCP

mcp_server = FastMCP(name="ServerMCP-Example")


@mcp_server.tool(
    name="listar-datos-ejemplo",
    description="Lista datos de ejemplo.",
    enabled=True,
    tags={"tool"},
    meta={"version": "1.0", "author": "Brayan"}
)
async def listar_datos_ejemplo():
    datos = [
        {"id": 1, "nombre": "Dato 1"},
        {"id": 2, "nombre": "Dato 2"},
        {"id": 3, "nombre": "Dato 3"},
    ]
    return datos

if __name__ == "__main__":
    mcp_server.run(host="0.0.0.0", port=8000,transport="http")
    
## Verificar servidor MCP
# Para verificar que el servidor MCP está funcionando correctamente, 
# puedes abrir tu navegador web y navegar a
# http://localhost:8000/mcp