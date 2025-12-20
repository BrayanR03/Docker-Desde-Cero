## ======== IMAGENES EN DOCKER ======== ##
# PASOS A SEGUIR:

# Paso 1. Crear un archivo llamado Dockerfile sin extensión (ya lo creamos).
# Paso 2. Definir la imagen base que vamos a utilizar (python:3.12-slim).
FROM python:3.12-slim

# 3. Establecer el directorio de trabajo dentro del contenedor (Podemos definir cualquier nombre).
WORKDIR /project_fastapi

# Paso 4. Copiar los archivos necesarios para instalar las dependencias (requirements.txt) 
#         al espacio de trabajo definido anteriormente (Paso 3).
COPY requirements.txt .
    
# Paso 5. Instalar las dependencias gracias al requirements.txt copiado en el paso anterior (Paso 4).
RUN pip install --no-cache-dir -r requirements.txt

# Paso 6. Copiar el resto de los archivos de la aplicación al contenedor definido anteriormente (Paso 3).
COPY . ./app/

# Paso 7. Exponer el puerto en el que se ejecutará la aplicación dentro del contenedor (Solo es necesario para la documentación).
EXPOSE 8000

# Paso 8. Definir los comandos para ejecutar la aplicación cuando se inicie el contenedor (Dependerá la tecnología que se use).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


## COMADOS PARA CONSTRUIR LA IMAGEN Y EJECUTAR EL CONTENEDOR:

#1.  Construir la imagen desde el Dockerfile (Ejecutar en la terminal/cmd en
# la ruta donde se encuentra el Dockerfile): 

# docker build -t nombre_imagen .


#2.  Ejecutar el contenedor desde la imagen creada (Ejecutar en la terminal/cmd):
# docker run -d --name nombre_contenedor -p 8000:8000  nombre_imagen

#3. Ejecutar el contenedor con volumenes mapeados (imagen de postgres como ejemplo):
# docker run -d \
# --name postgres_contenedor \
# -p 5432:5432 \
# -e POSTGRES_PASSWORD=admin123 \
# -v Code\03_port_mapping_volumenes\volumen_local:/var/lib/postgresql/18/docker \
# postgres