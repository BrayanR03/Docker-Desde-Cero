 # Port Mapping y Volúmenes en Docker 🐳

## 🌐 Port Mapping en Docker

El **Port Mapping** permite **redireccionar puertos** entre la máquina host y el contenedor.  
Esto hace posible acceder a los servicios que corren dentro del contenedor desde el exterior.

### ❌ Ejemplo sin port mapping:
```bash
docker run -d fastapi_imagen
```
* El contenedor usa el puerto interno definido en la imagen (en este caso 8000).

* Sin embargo, no hay forma de acceder externamente, debido que el puerto no está mapeado hacia la máquina host, es decir, fuera del contenedor.

### ✅ Ejemplo con port mapping:
```bash
docker run -d  -p 8000:8000 fastapi_imagen
```

* El puerto 8000 de nuestra máquina local redirige el tráfico entrante al puerto 8000 del contenedor.

* De esta forma, cualquier conexión externa llega al contenedor.

---

### 💾 Volúmenes en Docker

Los volúmenes funcionan de forma similar al port mapping, pero en lugar de mapear puertos, mapean carpetas o directorios.

Esto permite que los datos persistan en el sistema host, incluso si el contenedor se elimina o se reconstruye.

### 🧠 Concepto clave:

En la mayoría de casuísticas utilizamos los volúmenes de docker en las bases de datos, donde cada motor de base de datos (PostgreSQL, MySQL, MongoDB, etc.) tiene su ruta interna donde guarda los datos.

Ejemplo en PostgreSQL:
```bash
/var/lib/postgresql/18/docker
```
En esta carpeta es donde se almacenan los datos/configuraciones de PostgreSQL en el contenedor. Sin embargo, cada vez que borremos el contenedor y lo ejecutemos de nuevo, toda la información almacenada **SE PERDERÁ**.

### ✅ Sintaxis: volumen persistente
```bash
docker run -d \
  --name nombre_contenedor \
  -p puerto_maquina_local:puerto_contenedor \
  -e variable_entorno_segun_imagen \
  -v path_maquina_local:/var/lib/postgresql/18/docker \
  nombre_imagen
```
Donde:

* `-d` ejecuta el contenedor en segundo plano (detached mode).

* `--name nombre_contenedor` define el nombre del contenedor.

* `-p` mapea el puerto del contenedor hacia la máquina local (port-mapping).

* `-e` define variables de entorno necesarias para la configuración del contenedor(según la imagen).

* `-v` define el volumen que mapea la carpeta local a la ruta de datos del contenedor.

* `nombre_imagen` corresponde a la imagen desde la cual se crea el contenedor.



### ✅ Ejemplo: volumen persistente
```bash
docker run -d \
  --name postgres_contenedor \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=admin123 \
  -v Code\03_port_mapping_volumenes\volumen_local:/var/lib/postgresql/18/docker \
  portgres
```
Detalles del ejemplo:
* En este caso, el comando anterior permitirá ejecutar en segundo plano un contenedor de PostgreSQL (imagen previamente descargada mediante `docker pull postgres`).
* Las variables de entorno `POSTGRES_PASSWORD` se define como parte de la configuración adicional a la imagen `postgres`.
* El volumen mapea la carpeta local `Code\03_port_mapping_volumenes\volumen_local` a la ruta interna del contenedor donde PostgreSQL guarda sus datos. En caso no funcione la ruta relativa, se puede usar la ruta absoluta.
* De esta forma, los datos de PostgreSQL persistirán en la carpeta local, incluso si el contenedor se elimina o se vuelve a crear.

> 💡 **Nota:** Esta forma de ejecución del contenedor nos brinda un indicio de como se configuran los contenedores en entornos reales. Sin embargo, en próximos capítulos abarcaremos `docker-compose` el cuál nos permitirá definir explícitamente cada paso, desde la construcción/descarga de una imagen docker hasta la ejecución del contenedor con solo un simple comando.

### 📓 Resumen general
| Concepto                     | Qué hace                                                      | Ejemplo                         |
| ---------------------------- | ------------------------------------------------------------- | ------------------------------- |
| **Port Mapping (-p)**        | Conecta puertos del host y contenedor.                        | `-p 5400:5432`                  |
| **Volumen (-v)**             | Conecta carpetas host ↔ contenedor para persistencia.         | `-v ruta_host:ruta_contenedor`  |
| **Variable de entorno (-e)** | Configura parámetros dentro del contenedor (ej. contraseñas). | `-e POSTGRES_PASSWORD=admin123` |

### 🔍 Conclusión:
El uso conjunto de -p, -v y -e te permite construir contenedores persistentes, configurables y accesibles, replicando entornos reales de desarrollo o producción con facilidad.
 