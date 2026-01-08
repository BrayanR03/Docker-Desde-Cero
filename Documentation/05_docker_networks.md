# 🐳 Docker Networks 🌐

## Introducción

* Por defecto, al definir un docker-compose.yml, todos los servicios (contenedores) se ven entre sí, debido que comparten una red por defecto.

* Sin embargo, esto no es recomendable para producción, porque ciertos servicios deben estar aislados y expuestos solo a los servicios que realmente los necesitan.

* Entonces, las redes en Docker definen cómo los contenedores se aíslan o se comunican entre sí. Asimismo, en un Docker Compose, cada servicio forma parte de una red que permite la comunicación interna por nombre de servicio, manteniendo el aislamiento del resto del sistema.
* 🗃️ Archivo docker-compose básico de ejemplo en:
[05_docker_networks](https://github.com/BrayanR03/Docker-Desde-Cero/tree/main/Code/05_docker_networks)

---

## Tipos de redes en Docker

Docker ofrece 5 tipos de redes, cada una con características específicas:

### 1️⃣ Bridge (por defecto)

* Docker crea una red interna dentro del host.

* Cada contenedor recibe una IP interna para comunicarse con otros servicios.

* Las IP internas se traducen mediante NAT para acceder desde el exterior.

* Ejemplo de flujo:

```rust
HOST: 192.168.1.100 -> NAT -> CONTENEDORES: 172.18.0.X
```
* Uso recomendado: comunicación interna entre contenedores, buena para desarrollo.

---

### 2️⃣ Host

* El contenedor comparte la red del host directamente.

* No se realiza NAT, y cada servicio escucha en un puerto distinto.

* Ejemplo de flujo:

```rust
HOST: 192.168.1.100 -> SERV1: 192.168.1.12:5432 -> SERV2: 192.168.1.13:12345
```
* Uso recomendado: cuando quieres máxima performance de red y no necesitas aislamiento de IP.

---

### 3️⃣ None

* El contenedor no tiene acceso a ninguna red.

* Está completamente aislado.

* Uso recomendado: servicios que no necesitan comunicación de red.

---

### 4️⃣ Macvlan

* Permite que cada contenedor tenga su propia dirección MAC e IP en la red física.

* Cada contenedor puede comportarse como una máquina física separada.

* Uso recomendado: escenarios avanzados de virtualización de red.

---

### 5️⃣ Overlay

* Para redes que conectan contenedores en múltiples hosts, muy usado en Docker Swarm.

---

## Configuración de redes en Docker Compose

### 1. Definir redes en docker-compose.yml

```rust
networks:
  nombre_red_uno:
  nombre_red_dos:
```

### 2. Asignar redes a los servicios

```rust
services:
  nombre_servicio:
    image: referencia_imagen
    volumes:
      - volumen_contenedor:volumen_imagen
    depends_on:
      - nombre_servicio_dependencia
    networks:
      - nombre_red_uno
      - nombre_red_dos
```
  * ✅ Por defecto, las redes serán de tipo bridge.

---

## En conclusión

Docker Compose es como un rompecabezas:
Se definen servicios (contenedores), imágenes, redes, volúmenes y variables de entorno, y Docker Compose se encarga de levantar el sistema completo de manera coordinada.

---
