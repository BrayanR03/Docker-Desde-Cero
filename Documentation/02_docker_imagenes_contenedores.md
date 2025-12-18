# Imágenes y Contenedores en Docker 🐳

Las **imágenes** y **contenedores** son los **dos componentes fundamentales** del ecosistema Docker.  
Entender su diferencia es esencial para comprender cómo funcionan los sistemas dockerizados.

👉 Ejemplo en la siguiente carpeta: [Imagenes y Contenedores](https://github.com/BrayanR03/Docker-Desde-Cero/tree/main/Code/02_docker_images_contenedores)

---

## 🧱 Docker Images (Imágenes)

### ¿Qué es una imagen?
Una **Docker Image** es un **paquete de sólo lectura** que contiene **todo lo necesario para ejecutar una aplicación**, incluyendo:
- Sistema de archivos base.  
- Librerías y dependencias.  
- Código fuente y configuraciones.  

Se puede comparar con una **clase** en Programación Orientada a Objetos:  
cada vez que se ejecuta una imagen, se crea una **instancia** llamada **contenedor**.

📘 **Ejemplo:**
> De una sola imagen de PostgreSQL, puedes crear varias instancias (contenedores):  
> - BD de Pruebas  
> - BD de QA  
> - BD de Producción  

---

### 📦 ¿Dónde se almacenan las imágenes?

Las imágenes se guardan en **Docker Registries** (repositorios).  
Los más conocidos son:

- [**Docker Hub**](https://hub.docker.com) — Registro oficial y más usado.  
- **GitHub Container Registry**  
- **Google Container Registry (GCR)**  
- **Amazon ECR (Elastic Container Registry)**

El flujo básico es:
1. Extraer una imagen desde un registry (por ejemplo, Docker Hub).  
2. Descargarla a tu máquina.  
3. Crear un contenedor a partir de ella.

---

### 🛠️ Creación de imágenes personalizadas: Dockerfile

Cuando necesitas construir tus **propias imágenes**, usas un **Dockerfile**.  
Es un archivo de texto plano que contiene **instrucciones secuenciales** para construir una imagen Docker.

**Definición:**
> Un Dockerfile es un conjunto de instrucciones que Docker usa para **generar imágenes personalizadas** y luego **crear contenedores** a partir de ellas.

---

## 🚀 Simulación: Desplegar una aplicación manualmente (sin Dockerfile)

Este proceso ayuda a entender cómo se levantaría una aplicación manualmente dentro de un contenedor (ejemplo: **FastAPI**).

### 🔹 Pasos

1. **Abrir Docker Desktop** (asegurarse de que el daemon esté corriendo).
2. **Descargar una imagen base:**
   ```bash
   docker pull ubuntu
   ```
   (por defecto descarga la última versión disponible)
3. Revisar imágenes descargadas:
  ```bash
  docker images
  ```
4. Ejecutar la imagen de forma interactiva:
  ```bash
  docker run -it -p 8000:8000 ubuntu
  ```
  Esto te “mete” dentro del contenedor, simulando un servidor Ubuntu dockerizado.

---
### 🧩 Subpasos dentro del contenedor (servidor Ubuntu simulado)
| Paso  | Comando / Acción                                             | Descripción                                      |
| ----- | ------------------------------------------------------------ | ------------------------------------------------ |
| i.    | `apt-get update`                                             | Actualiza los registros del sistema.             |
| ii.   | `apt-get install -y python3`                                 | Instala dependencias necesarias.                 |
| iii.  | `mkdir app`                                                  | Crea el directorio donde desplegarás tu app.     |
| iv.   | `apt-get install -y python3-pip`                             | Instala `pip`.                                   |
| v.    | `apt-get install -y nano`                                    | Instala un editor de texto.                      |
| vi.   | `nano requirements.txt`                                      | Crea archivo de dependencias.                    |
| vii.  | `pip3 install -r requirements.txt --break-system-packages`   | Instala dependencias (omitimos entorno virtual). |
| viii. | `python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000` | Levanta el servidor FastAPI.                     |
| ix.   | `exit`                                                       | Salimos del contenedor.                          |

  💡 Nota: Las imágenes Docker son ligeras a propósito, por lo que muchas herramientas no vienen preinstaladas.

---

### 🧰 Despliegue automático con Dockerfile

En lugar de ejecutar todos los pasos manualmente, podemos automatizarlos mediante un Dockerfile. ***Inicialmente en los sistemas operativos (Windows y Mac) debemos iniciar Docker Desktop.***

🔹 Pasos para crear y ejecutar un contenedor con Dockerfile

1. Creamos archivo:
    ```bash
    Dockerfile
    ```
    
2. Definimos imagen base:
    ```bash
    FROM ubuntu:22.04
    ```
    
3. Instalamos dependencias (en caso sea necesario):
    ```bash
    RUN apt-get update && apt-get install -y python3 python3-pip
    ```
    
4. Definimos directorio de trabajo (Puede ser `app` u otro nombre):
    ```bash
    WORKDIR /app
    ```
    
5. Copiamos los requerimientos:
    ```bash
    COPY requirements.txt .
    ```
6. Instalamos las dependencias definidas en el archivo `requirements.txt`:
    ```bash
    RUN pip3 install -r requirements.txt
    ```
7. Copiamos el código de la aplicación

    ```bash
    COPY . .
    ```
    **¿Qué indican los puntos (`.`) en el Dockerfile?**

    Los puntos indican la ruta de origen y destino:

    * El primer `.` representa la raíz del proyecto en la máquina local.

    * El segundo `.` representa el directorio de trabajo (`WORKDIR`) dentro del contenedor.

    Supongamos que tenemos la siguiente estructura de proyecto:
    ```bash
      proyecto_carpeta/
      ├─ app/
      ├─ main.py
      ├─ requirements.txt
      ├─ Dockerfile
    ```
    Al usar:
    ```yml
    COPY . .
    ```
    Docker copiará todo el contenido de `proyecto_carpeta` hacia el `WORKDIR` definido en el contenedor, incluyendo:

    * `app/`

    * `main.py`

    * `requirements.txt`

    * `Dockerfile`

    El resultado dentro del contenedor será:
    ```bash
      nombre_workdir_dockerfile/
      ├─ app/
      ├─ main.py
      ├─ requirements.txt
      ├─ Dockerfile
    ```  
  
    📁 Copiar carpetas específicas con `COPY`

    En algunos casos (dependiendo de la arquitectura del proyecto), no conviene copiar todo el contenido, sino únicamente carpetas específicas.

    Por ejemplo, si definimos en el Dockerfile:
    
    ```yml
      COPY app/ ./app/
    ```
    Aquí:

    * `app/` (primer valor) apunta a la carpeta del proyecto local.

    * `./app/` (segundo valor) indica una carpeta dentro del contenedor.

    Si dicha carpeta no existe, Docker la crea automáticamente.

    Dado el siguiente proyecto local:
    ```bash
    proyecto_carpeta/
    ├─ app/
    ├─ main.py
    ├─ requirements.txt
    ├─ Dockerfile
    ```
    El resultado dentro del contenedor será:
    ```css
    nombre_workdir_dockerfile/
    ├─ app/
    │   └─ app/
        ├─ main.py
        ├─ requirements.txt
        ├─ Dockerfile
    ```
    ⚠️ Consideración importante

    Esta estructura puede obligarnos a modificar los imports del proyecto, agregando un prefijo adicional, por ejemplo:
    ```python
    from app.clientes import router
    ```
    Por este motivo, en la mayoría de proyectos simples o medianos, se prefiere utilizar:
    ```yml
    COPY . .
    ```
    debido que mantiene la misma estructura del proyecto original y evita ajustes innecesarios en los imports.


8. Comando para ejecitar servidor:
    ```bash
    CMD ["python3", "-m", "uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]
    ```
9. Construimos imagen:
    ```bash
    docker build -t nombre_imagen .
    ```
10. Verificamos imágenes construidas:
    ```bash
    docker images
    ```
    Si todo salió bien, se verá el detalle de la imagen creada:


11. Ejecutamos el contenedor (sintaxis básica):
    ```bash
    docker run -d -p 8000:8000 nombre_imagen
    ```
12. Verificamos que el contenedor este en ejecución
    ```bash
    docker ps
    ```
    
    ✅ Verifica en tu navegador:
    http://localhost:8000


---

### ☁️ Subir tu imagen a Docker Hub

1. Construir imagen con tu usuario de Docker Hub:
    ```bash
      docker build -t usuario_docker/nombre_imagen .
    ```
2. Iniciar sesión:
    ```bash
      docker login
    ```
2. Subir imagen:
    ```bash
      docker push usuario_docker/nombre_imagen
    ```
  Tu imagen ahora está disponible en la nube y puede descargarse desde cualquier equipo con Docker.

---

## 📦 Contenedores

Los contenedores permiten **aislar una aplicación** junto con todas sus librerías, dependencias y configuraciones, tal como fueron definidas previamente en el **Dockerfile**.

Un contenedor no es más que una **instancia en ejecución de una imagen Docker**, y es el responsable de ejecutar el proceso principal de la aplicación (por ejemplo, un servidor web o una API).

De forma básica, un contenedor Docker puede ejecutarse con el siguiente comando:

```bash
docker run -d -p 8000:8000 nombre_imagen
```
Donde:

* `-d` ejecuta el contenedor en segundo plano (detached mode).

* `-p 8000:8000` expone el puerto del contenedor hacia el sistema anfitrión.

* `nombre_imagen` corresponde a la imagen desde la cual se crea el contenedor.

Docker permite definir muchos más parámetros al momento de ejecutar un contenedor (volúmenes, variables de entorno, redes, límites de recursos, entre otros), los cuales se irán abordando progresivamente en capítulos posteriores.
Además, estos son algunos comando primordiales al utilizar contenedores docker:

a). Verificar contenedores en ejecución (Obtenemos contenedor_id, image, entre otros)  
```bash
docker ps
```

b). Verificar estado de contenedores por error de ejecución o detenidos (Obtenemos contenedor_id, image, entre otros) 
```bash
docker ps -a
```

c). Detener ejecución de un contenedor
```bash
docker stop contenedor_id
```

d). Eliminar un contenedor
```bash
docker rm contenedor_id
```

d). Detener y eliminar un contenedor (forzar)
```bash
docker rm contenedor_id -f
```


### Resumen conceptual
| Concepto       | Descripción                                                             |
| -------------- | ----------------------------------------------------------------------- |
| **Imagen**     | Paquete inmutable que contiene todo lo necesario para ejecutar una app. |
| **Contenedor** | Instancia ejecutable de una imagen (mutable).                           |
| **Dockerfile** | Archivo de texto con instrucciones para construir una imagen.           |
| **Registry**   | Repositorio donde se almacenan imágenes Docker (ej. Docker Hub).        |
