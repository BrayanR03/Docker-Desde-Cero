# Paso A). Definir la imagen base
FROM python:3.11-slim

# Paso B). Establecer el directorio de trabajo
WORKDIR /fastmcp_project

# Paso C). Copiar el archivo de dependencias
COPY requirements.txt .

# Paso D). Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Paso E). Copiar el código fuente de la aplicación
COPY . .

# Paso F). Exponer el puerto en el que la aplicación escuchará
EXPOSE 8000

# Paso G). Definir el comando para ejecutar la aplicación
CMD ["python", "main.py"]