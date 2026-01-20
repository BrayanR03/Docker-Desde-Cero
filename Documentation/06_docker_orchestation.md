# Capítulo 6: Docker Orchestration – Bases
## Introducción
Uno de los grandes problemas que enfrenta Docker en entornos reales es el escalado:

* Con Docker Compose, cada servicio se ejecuta en uno o más contenedores, pero si la cantidad de usuarios supera la capacidad estimada, el escalado debe realizarse de forma manual.

* Además, Docker Compose está pensado principalmente para desarrollo y entornos controlados, no para infraestructura distribuida.

👉 La solución moderna a este problema es la orquestación de contenedores, que permite administrar múltiples contenedores y nodos de forma automática, inteligente y escalable.

---

## 🧠 ¿Qué es la orquestación de contenedores?
La orquestación de contenedores es el proceso de gestionar automáticamente:

* El despliegue de contenedores

* El escalado de servicios

* La comunicación entre contenedores

* La alta disponibilidad

* La recuperación ante fallos

Todo esto sobre múltiples nodos, como si fueran un solo sistema lógico (cluster). En otras palabras, un orquestador decide:

* Dónde se ejecuta cada contenedor

* Cuántas réplicas deben existir

* Qué hacer si un nodo falla

* Cómo balancear la carga entre servicios

---

## ⚙️ Tecnologías de orquestación
| Tecnología   | Características                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------- |
| Docker Swarm | Orquestador **nativo de Docker**, fácil de configurar, permite clusters y alta disponibilidad.      |
| Kubernetes   | Más reciente y poderosa, curva de aprendizaje elevada, autoescalamiento avanzado y gran ecosistema. |
> 📌 En esta serie nos enfocamos en un ejemplo a mano alsada sobre Docker Swarm como introducción a la orquestación, sin entrar en Kubernetes.
---
## 🐳 Docker Swarm
Docker Swarm es el orquestador nativo de Docker, integrado directamente en el Docker Engine.

Permite:

* Crear y administrar clusters de contenedores

* Gestionar múltiples nodos como un solo sistema

* Garantizar alta disponibilidad, seguridad y escalabilidad

🧱 Arquitectura base recomendada

* 3 nodos Manager

    * 1 líder principal

    * 2 nodos de respaldo (alta disponibilidad)

* 3 nodos Worker

    * Ejecutan los contenedores (servicios)

Cada nodo puede ser un servidor físico o virtual.

---

## 🔌 Puertos utilizados por Docker Swarm
| Puerto       | Uso                        |
| ------------ | -------------------------- |
| 2377/TCP     | Comunicación del cluster   |
| 7946/TCP/UDP | Comunicación entre nodos   |
| 4789/UDP     | Tráfico de overlay network |
Estos puertos permiten la coordinación, descubrimiento y comunicación interna del cluster.

---

## Pasos para iniciar un cluster Docker Swarm
### 1️⃣ Inicializar el nodo Manager

1. Conectarse al servidor líder (Manager):
```bash
ssh usuario@192.168.X.X
```
2. Inicializar Swarm:
```bash
docker swarm init --advertise-addr 192.168.X.X
```
* Si el servidor tiene varias interfaces de red, especificar la IP correcta con --advertise-addr.

3.  Swarm retornará un token para unirse como Worker.

---

### 2️⃣ Verificar estado del Swarm
```bash
docker node ls
```
---

### 3️⃣ Agregar nodos Worker

1. Conectarse a cada nodo Worker:
```bash
ssh usuario@192.168.X.X
```
2. Unirse al Swarm usando el token proporcionado por el nodo Manager:
```bash
docker swarm join --token SWMTKN-1-XXXXX 192.168.X.X:2377
```
3. Verificar estado desde el Manager:
```bash
docker node ls
```
* Con esto, tendrás 1 Manager y 3 Workers configurados.
---

### 4️⃣ Agregar nodos Manager adicionales

1. Desde el Manager principal, obtener el token para nuevos Managers:
```bash
docker swarm join-token manager
```
2. Se retornará algo como:
```bash
docker swarm join --token SWMTKN-1-XXXX 192.168.X.X:2377
```
3. Conectarse a cada nodo Manager de respaldo y ejecutar el comando anterior.
4. Verificar estado:
```bash
docker node ls
```
---
## 🧠 Conceptos clave de Docker Swarm
* Un cluster agrupa múltiples nodos bajo una sola administración.

* Los Managers controlan el estado del cluster.

* Los Workers ejecutan los contenedores.

* Los servicios pueden escalarse automáticamente mediante réplicas.

* Si un nodo falla, Swarm redistribuye los contenedores.

---

## ⚖️ Ventajas y similitudes de Docker Swarm
✅ Ventajas de Docker Swarm

* Integración nativa con Docker

* Configuración sencilla

* Menor curva de aprendizaje

* Ideal como primer acercamiento a la orquestación

* Soporta balanceo de carga y alta disponibilidad

🔁 Similitudes con otros orquestadores

* Uso de clusters

* Separación de nodos de control y ejecución

* Comunicación mediante redes overlay

* Escalado de servicios

* Alta disponibilidad

---
## 🎯 Conclusión

Docker Swarm permite dar el siguiente paso después de Docker Compose:
pasar de contenedores aislados a infraestructura distribuida.

Es una excelente herramienta para entender los fundamentos de la orquestación de contenedores, el escalado y la alta disponibilidad, sirviendo como base conceptual antes de explorar soluciones más complejas.

Con este capítulo, se cierra el ciclo inicial de Docker:
contenedores → imágenes → volúmenes → redes → orquestación 🐳🚀
