# XIOMEX_TECH

## Descripción

**XIOMEX_TECH** es una aplicación web tipo **e-commerce** enfocada en la venta de productos tecnológicos e incluye un apartado publicitario para promocionar los servicios ofrecidos por el negocio, como reparación y mantenimiento de dispositivos electrónicos. El proyecto está siendo desarrollado con **Django**, **MySQL**, **HTML**, **CSS** y **JavaScript**.

---

# Bitácora de desarrollo

## Estado #1 - Registro y autenticación

**Fecha:** 27/07/2026

### Estado actual

En esta etapa del desarrollo ya se encuentra implementado el módulo de **registro y autenticación de usuarios**, incluyendo la interfaz y la conexión con la base de datos.

El resto de las vistas disponibles en la aplicación son actualmente **prototipos estáticos**, utilizados como referencia visual para mostrar la estructura, el diseño y la dirección que tomará el proyecto durante las siguientes fases de desarrollo.

### Próximo paso

Continuar con el desarrollo del **módulo de perfil de usuario**, implementando su interfaz, funcionalidades y conexión con la base de datos.

---

## Estado #2 - Perfil, seguridad y recuperación de contraseña

**Fecha:** 21/08/2026

### Estado actual

En esta etapa se desarrolló el **módulo de perfil de usuario**, incluyendo la consulta de los datos almacenados en la base de datos, visualización de información personal, cambio de fotografía de perfil y edición de los datos del usuario.

También se implementó el apartado de **seguridad**, desde el cual el usuario puede gestionar el cambio de su contraseña.

Además, se desarrolló el proceso de **recuperación de contraseña mediante correo electrónico**, incorporando:

* Solicitud de recuperación mediante correo.
* Generación y envío de un **código de verificación de 6 dígitos**.
* Tiempo de expiración del código.
* Verificación del código recibido.
* Acceso al formulario para establecer una nueva contraseña.
* Protección del proceso mediante datos almacenados temporalmente en la sesión.
* Visualización y ocultamiento de las contraseñas mediante un botón.

El proceso de **registro de usuarios** también fue complementado con la verificación del correo electrónico mediante un código de 6 dígitos antes de crear definitivamente la cuenta.

En cuanto a la interfaz, se continuó unificando el diseño de las vistas mediante los estilos generales del proyecto, utilizando la paleta de colores definida para **XIOMEX_TECH** y componentes reutilizables.

### Próximo paso

Continuar con el desarrollo de las funcionalidades principales del **e-commerce**, comenzando por el módulo de **productos e inventario**, para posteriormente avanzar hacia el carrito de compras, pedidos y demás funcionalidades del sistema.

---

> Esta bitácora se actualizará conforme avance el desarrollo del proyecto.
