# 🐳🦑 Docker Compose
## 📘 ¿Qué es Docker Compose?

Docker Compose es una herramienta que permite definir y ejecutar aplicaciones multicontenedor.
Con un solo comando (docker-compose up), puedes levantar todo un stack (por ejemplo: backend + frontend + base de datos) definido en un solo archivo YAML.

📄 **Archivo principal**: `docker-compose.yml`

🗃️ Archivo docker-compose básico de ejemplo en:
[04_docker_compose](https://github.com/BrayanR03/Docker-Desde-Cero/tree/main/Code/04_docker_compose)

Archivo docker-compose completo de ejemplo en:
[FastAPI-Dockerizado](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_clientes/docker-compose.yml)

---

## ⚙️ Estructura del archivo docker-compose.yml
### 🧩 Paso A: Definimos la versión del esquema de Compose
```yaml
version: "3.9" ## En la mayoría de los casos, usar la versión más reciente es recomendable.
```
* 💡 La versión define el formato de configuración y las características compatibles con el motor Docker.

### 🧱 Paso B: Definir los servicios

Cada servicio representa un contenedor dentro de la aplicación.
* Ejemplo - Sintaxis 1: (docker-compose con una imagen local definida por un Dockerfile)
```yaml
services:
  nombre_servicio:               # Nombre del servicio o contenedor
    build: ubicacion_dockerfile  # *build* nos permite crear la imagen a partir de un Dockerfile
    ports:
      - "puerto_maquina_local:puerto_contenedor" # *ports* permite el port-mapping
    depends_on:
      - nombre_otro_servicio  # *depends_on* define que este servicio depende de otro servicio
    environment:
      - NOMBRE_VARIABLE=valor  # *environment* define las variables de entorno
    volumes:
      - nombre_volumen  # *volumes* permite establecer el volumen para la persistencia de datos (Volumen internamente definido)
```

* Ejemplo - Sintaxis 2: (docker-compose con una imagen desde Docker Hub)
```yaml
services:
  nombre_servicio:               # Nombre del servicio o contenedor
    image: nombre_imagen # *image* Permite descargar una imagen existente del Docker Hub.
    ports:
      - "puerto_maquina_local:puerto_contenedor" # *ports* permite el port-mapping
    depends_on:
      - nombre_otro_servicio  # *depends_on* define que este servicio depende de otro servicio
    environment:
      - NOMBRE_VARIABLE=valor  # *environment* define las variables de entorno
    volumes:
      - nombre_volumen  # *volumes* permite establecer el volumen para la persistencia de datos (Volumen internamente definido)
```

---

## ▶️ Ejecución de Docker Compose

| Comando                     | Descripción                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------- |
| `docker-compose up --build` | Construye las imágenes y levanta los contenedores. Se usa la primera vez o tras modificar el Dockerfile. |
| `docker-compose up`         | Levanta los contenedores con las imágenes ya construidas (bloquea la terminal).                                                |
| `docker-compose down`       | Detiene y elimina los contenedores, redes y volúmenes (no borra las imágenes).                           |
| `docker-compose ps`         | Lista los servicios levantados por el Compose.                                                           |
| `docker-compose logs`       | Muestra los logs de todos los servicios.                                                                 |
| `docker-compose up -d` | Al momento de ejecutar la configuración de docker-compose, no bloquea la terminal.

---

## 🧠 Conceptos Clave

* build: se usa cuando quieres crear una imagen desde tu propio Dockerfile.

* image: se usa cuando quieres descargar una imagen existente del Docker Hub u otro registro.

* depends_on: establece el orden de inicio, pero no garantiza que el servicio esté “listo” (por ejemplo, que la DB haya inicializado).

* environment: define variables de entorno dentro del contenedor.

* volumes: permiten persistir datos o compartir archivos entre contenedores y el sistema host.

---

## 🧩 Ejemplo Visual (Arquitectura)
```pgsql
+------------------------------------------+
|        Docker Compose                    |
+------------------------------------------+
| Services:                                |
|  - nombre_servicio_uno  --> Flask App    |
|  - nombre_servicio_dos   --> PostgreSQL  |
+------------------------------------------+
| Shared Volumes (nombre_volumen)          |
| Shared Network (bridge por defecto)      |
+------------------------------------------+
```

---

## ✅ Buenas prácticas

* Usa nombres descriptivos para tus servicios (web, db, redis, etc.).

* Define variables sensibles en un archivo .env y cárgalas en Compose.

* Evita exponer todos los puertos si no es necesario.

* Usa docker-compose down -v con precaución (elimina volúmenes de datos).

* Documenta tu stack con comentarios claros en el YAML.
