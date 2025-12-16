# Introducción a Docker

Docker es una plataforma para empaquetar, distribuir y ejecutar aplicaciones en contenedores ligeros y reproducibles. En esta introducción veremos por qué surgieron los contenedores, cómo encajan en la evolución tecnológica (máquinas virtuales → entornos virtuales de lenguaje → contenedores) y las diferencias prácticas entre ejecutarlos en Linux vs. Windows/macOS.

---

## Problemas antes de Docker
- En un mismo host las aplicaciones compartían librerías, binarios y versiones del sistema, lo que provocaba conflictos difíciles de reproducir y arreglar.
- La solución tradicional fueron las máquinas virtuales (VMs), que aíslan aplicaciones con sistemas operativos completos, pero tienen desventajas: mayor consumo de recursos, tiempos de arranque más largos y mayor complejidad para replicar entornos ligeros.

---

## Línea de tiempo y contexto (por qué evolucionamos así)
1. Máquinas virtuales (VMs): cada aplicación tenía su propio sistema operativo. Aislan bien, pero son pesadas (overhead de CPU/RAM/almacenamiento) y lentas de desplegar.
2. Entornos virtuales de lenguaje (ej. Python `venv`, `pipenv`): resuelven dependencia de paquetes a nivel de lenguaje, pero no aíslan diferencias de sistema operativo ni del kernel (p. ej. versiones de libc, demonios del sistema, servicios del SO).
3. Contenedores (Docker): combinan lo mejor de ambos mundos: aislamiento y reproducibilidad con un coste muy inferior al de una VM, porque los contenedores comparten el kernel del host y utilizan espacios de nombres (namespaces) y control de recursos (cgroups) para aislar procesos, redes y sistemas de archivos.

> Resultado: Docker permite «construir una vez, ejecutar en cualquier lugar» siempre que el kernel sea compatible (o haya una capa que provea esa compatibilidad).

---

## ¿Qué es Docker? — concepto clave
- **Imagen:** plantilla inmutable que contiene el sistema de archivos necesario para ejecutar una aplicación (binarios, librerías, configuración). Se define típicamente mediante un `Dockerfile`.
- **Contenedor:** instancia en ejecución de una imagen; aislada a nivel de procesos, red y sistema de archivos pero comparte el kernel del host.
- **Docker Engine (daemon `dockerd`):** servicio que gestiona la creación, ejecución y supervisión de contenedores. El cliente `docker` se comunica con el daemon.
- **Registro (Registry):** servicio donde se almacenan imágenes (por ejemplo Docker Hub, GitHub Container Registry).

---

## Docker en Linux vs Windows / macOS
**Linux (nativo):**
- Docker funciona de forma nativa en Linux porque usa funcionalidades del kernel (namespaces, cgroups, sistemas de archivos copy-on-write) para aislar contenedores.
- Los contenedores comparten el kernel del host, lo que hace que sean muy eficientes en arranque y uso de recursos.

**Windows / macOS (Docker Desktop):**
- Windows y macOS no exponen internamente el kernel Linux, que es el que Docker usa habitualmente. Por eso, Docker Desktop crea una máquina virtual ligera con kernel Linux para ejecutar contenedores Linux.
  - En Windows moderno, la integración se hace normalmente sobre WSL2 (Windows Subsystem for Linux 2) o, en otros entornos, Hyper-V.
  - En macOS se usa una VM ligera (p. ej. mediante HyperKit o el runtime de Apple) para ejecutar el kernel Linux.
- Implicaciones prácticas:
  - Rendimiento de I/O: las monturas de volumen entre host y la VM pueden ser más lentas que en Linux nativo; hay recomendaciones para mejorar el rendimiento (evitar montar millones de archivos desde el host, usar herramientas de sincronización, etc.).
  - Red y localhost: Docker Desktop mapea puertos para que `localhost` funcione en el host, pero el comportamiento puntual puede diferir (DNS, resolución, mapeo de puertos doble en algunos casos).
  - Recursos: Docker Desktop permite limitar CPU/memoria de la VM y, por tanto, de los contenedores.
- Nota sobre Windows Server: Windows también soporta contenedores nativos basados en el kernel de Windows (Windows Containers), pero la mayoría de imágenes en la práctica son Linux y requieren la VM.

---

## Arquitectura (simplificada)
```
Hardware
└─ Host OS Kernel (Linux nativo o kernel Linux dentro de una VM en macOS/Windows)
   └─ Docker Engine (dockerd)
      └─ Imágenes -> Contenedores (instancias aisladas)
```
- En Linux el kernel es el del sistema host; en macOS/Windows, el kernel Linux corre dentro de una VM que Docker Desktop administra.

## Instalación (recomendaciones rápidas)
- **Windows:** instalar Docker Desktop y activar WSL2 si está disponible (mejor rendimiento y compatibilidad). En Windows Server se puede usar Windows Containers de forma nativa.
- **macOS:** instalar Docker Desktop (requiere soporte de virtualización). 
- **Linux:** instalar el paquete oficial para tu distribución (p. ej. `apt`, `dnf`, `pacman`) o seguir la guía oficial.

---

## Primeros pasos en Docker
- Ejecutar un contenedor de ejemplo (Nginx):

```bash
docker run --name test -d -p 8080:80 nginx:alpine
```

Explicación breve:
- `--name test` → nombre del contenedor.
- `-d` → detached (ejecución en segundo plano).
- `-p 8080:80` → mapear puerto 80 del contenedor al puerto 8080 del host.

> La primera vez descargará la imagen `nginx:alpine` desde Docker Hub si no existe localmente. Luego expone el servicio en `http://localhost:8080`.

**Comandos útiles:**
- `docker images` → listar imágenes locales.
- `docker ps` → ver contenedores en ejecución.
- `docker ps -a` → ver todos los contenedores (activos + detenidos).
- `docker stop <id|name>` → detener contenedor.
- `docker rm <id|name>` → eliminar contenedor detenido.
- `docker rmi <imagen>` → eliminar imagen.
- `docker logs <id|name>` → ver logs del contenedor.

---

## Relación con entornos virtuales de Python
- Los entornos virtuales (`python -m venv .venv`, `pip install`) aíslan dependencias a nivel de lenguaje, pero no el sistema operativo ni servicios del sistema.
- Docker aísla a nivel de sistema (bibliotecas, utilidades y configuración), lo que mejora la reproducibilidad entre distintos entornos (desarrollo, CI, producción).

**Ejemplo breve:**
```bash
# Virtualenv (aislamiento a nivel de Python)
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
pip install -r requirements.txt

# Docker (aislamiento a nivel de sistema)
docker build -t miapp:1.0 .
docker run --rm -p 8000:8000 miapp:1.0
```

---
