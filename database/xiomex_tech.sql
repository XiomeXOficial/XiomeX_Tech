-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-07-2026 a las 20:14:06
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `xiomex_tech`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$ZzuGHTCRW2dtPc8L36f7x8$zUzmg3xR4af1gU/F0ZzWSFaAcbZB0VgwlL/mXCcUuAY=', '2026-06-10 17:44:48.812822', 1, 'Michael', '', '', 'Cmaicoljhoan@gmail.com', 1, 1, '2026-06-10 17:39:54.333446');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carritos`
--

CREATE TABLE `carritos` (
  `carr_id` int(11) NOT NULL COMMENT 'ID del carrito',
  `usu_id` int(11) NOT NULL COMMENT 'Dueño del carrito'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `catg_id` int(11) NOT NULL COMMENT 'ID de categoría',
  `catg_nombre` varchar(50) NOT NULL COMMENT 'Nombre de la categoría'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_carrito`
--

CREATE TABLE `detalle_carrito` (
  `detcarr_id` int(11) NOT NULL COMMENT 'ID del detalle',
  `detcarr_cantidad` int(11) NOT NULL COMMENT 'Cantidad agregada',
  `carr_id` int(11) NOT NULL COMMENT 'Carrito asociado',
  `prod_id` int(11) NOT NULL COMMENT 'Producto agregado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_pedido`
--

CREATE TABLE `detalle_pedido` (
  `detpedi_id` int(11) NOT NULL COMMENT 'ID del detalle',
  `detpedi_cantidad` int(11) NOT NULL COMMENT 'Cantidad comprada',
  `detpedi_precio` decimal(10,2) NOT NULL COMMENT 'Precio unitario',
  `pedi_id` int(11) NOT NULL COMMENT 'Pedido asociado',
  `prod_id` int(11) NOT NULL COMMENT 'Producto comprado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-06-10 17:13:16.852309'),
(2, 'auth', '0001_initial', '2026-06-10 17:13:17.297568'),
(3, 'admin', '0001_initial', '2026-06-10 17:13:17.389464'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-06-10 17:13:17.397704'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-06-10 17:13:17.407247'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-06-10 17:13:17.461137'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-06-10 17:13:17.508061'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-06-10 17:13:17.520932'),
(9, 'auth', '0004_alter_user_username_opts', '2026-06-10 17:13:17.527899'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-06-10 17:13:17.566852'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-06-10 17:13:17.570251'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-06-10 17:13:17.577291'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-06-10 17:13:17.591874'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-06-10 17:13:17.603481'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-06-10 17:13:17.616189'),
(16, 'auth', '0011_update_proxy_permissions', '2026-06-10 17:13:17.625414'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-06-10 17:13:17.641968'),
(18, 'sessions', '0001_initial', '2026-06-10 17:13:17.670231');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0mrizrx4zl1n1qmn7o2k12lqjpn1rxst', '.eJxVjDsOwyAQBe9CHSEQP5Eyfc6AlmU3OIlAMnZl5e4RkoukfTPzDpFg32raB61pKeIqtLj8bhnwRW2C8oT26BJ729Yly6nIkw5574Xet9P9O6gw6qwNF4tIpgBzIONUdIA6eqtIc-BcnEVvPSIgZczGOiIOPrMOysQgPl8k9DlY:1wXMyu:kFWNRSN6CGqDst2R9QCyDKuXur-8dNhoZ7z7-Qit9fo', '2026-06-24 17:44:48.815380'),
('8b1d7ebi19iwgryvmrwwxk70a6247nc7', '.eJyrViotLk0sysyPz0xRsjLWgXPz8nOTilKVrJS8ShPzUouVEDJF-TlA4eSczNS8klSlWgAa1Bei:1wo3rM:gd3ojCuMwUQfxyqJfZKrZs_MUTvpR0XoZmElnuZncbs', '2026-08-09 18:46:00.653381');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `pedi_id` int(11) NOT NULL COMMENT 'ID del pedido',
  `pedi_numero` varchar(30) NOT NULL COMMENT 'Número de referencia',
  `pedi_fecha` datetime NOT NULL COMMENT 'Fecha del pedido',
  `pedi_total` decimal(10,2) NOT NULL COMMENT 'Total de la compra',
  `pedi_metodo_pago` varchar(20) NOT NULL COMMENT 'Método de pago',
  `pedi_direccion` varchar(255) DEFAULT NULL COMMENT 'Dirección de entrega',
  `pedi_ciudad` varchar(50) DEFAULT NULL COMMENT 'Ciudad de entrega',
  `pedi_departamento` varchar(50) DEFAULT NULL COMMENT 'Departamento de entrega',
  `pedi_estado` varchar(20) NOT NULL COMMENT 'Estado del pedido',
  `usu_id` int(11) NOT NULL COMMENT 'Usuario comprador'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `prod_id` int(11) NOT NULL COMMENT 'ID del producto',
  `prod_nombre` varchar(100) NOT NULL COMMENT 'Nombre del producto',
  `prod_descripcion` text DEFAULT NULL COMMENT 'Descripción del producto',
  `prod_precio` decimal(10,2) NOT NULL COMMENT 'Precio de venta',
  `prod_stock` int(11) NOT NULL COMMENT 'Cantidad disponible',
  `prod_img` varchar(255) DEFAULT NULL COMMENT 'Ruta de imagen',
  `prod_estado` varchar(20) DEFAULT NULL COMMENT 'Estado del producto',
  `catg_id` int(11) DEFAULT NULL COMMENT 'Categoría asociada'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `serv_id` int(11) NOT NULL COMMENT 'ID del servicio',
  `serv_nombre` varchar(100) NOT NULL COMMENT 'Nombre del servicio',
  `serv_descripcion` text DEFAULT NULL COMMENT 'Descripción del servicio',
  `serv_telefono` varchar(20) DEFAULT NULL COMMENT 'Teléfono de contacto',
  `serv_img` varchar(255) DEFAULT NULL COMMENT 'Ruta de imagen',
  `serv_estado` varchar(20) DEFAULT NULL COMMENT 'Estado del servicio'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usu_id` int(11) NOT NULL COMMENT 'ID único del usuario',
  `usu_nombre` varchar(50) NOT NULL COMMENT 'Nombre(s) del usuario',
  `usu_apellido` varchar(50) DEFAULT NULL,
  `usu_rol` varchar(20) NOT NULL DEFAULT 'cliente' COMMENT 'Rol del usuario',
  `usu_telefono` varchar(20) DEFAULT NULL COMMENT 'Teléfono de contacto',
  `usu_correo` varchar(100) NOT NULL COMMENT 'Correo electrónico',
  `usu_contraseña` varchar(255) NOT NULL COMMENT 'Contraseña cifrada',
  `usu_img` varchar(255) DEFAULT 'default.png' COMMENT 'Ruta de foto de perfil'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usu_id`, `usu_nombre`, `usu_apellido`, `usu_rol`, `usu_telefono`, `usu_correo`, `usu_contraseña`, `usu_img`) VALUES
(1, 'Michael', 'Ceballos', 'cliente', '1234567890', 'Michael@gmail.com', 'pbkdf2_sha256$600000$VRMhkD9uhYez6V9ZCWxgy6$Nq1fm5AODVI3VqUvwJSQqVha93RYs/9ZJ9kJfDsAN8Q=', 'default.png'),
(2, 'Sofia', '', 'cliente', '', 'sofia@gmail.com', 'pbkdf2_sha256$600000$gMtX5NZ0OOgk9ndKBdSgrd$p8215f3q//oIFaPSgGcH1+31twd3EY5LdAWTnnAZ1WI=', 'default.png'),
(3, 'Juanes', 'Ocampo', 'cliente', '1234567890', 'Juanes@gmail.com', 'pbkdf2_sha256$600000$v9jpAljDH8MZD8JhZCXEv2$RbEePjWEnCzS+sytbqSscErk5y46AFXG4e3ir8DRrWk=', 'default.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `carritos`
--
ALTER TABLE `carritos`
  ADD PRIMARY KEY (`carr_id`),
  ADD KEY `fk_usuario_carrito` (`usu_id`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`catg_id`);

--
-- Indices de la tabla `detalle_carrito`
--
ALTER TABLE `detalle_carrito`
  ADD PRIMARY KEY (`detcarr_id`),
  ADD KEY `fk_carrito_detalle` (`carr_id`),
  ADD KEY `fk_producto_detalle_carrito` (`prod_id`);

--
-- Indices de la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  ADD PRIMARY KEY (`detpedi_id`),
  ADD KEY `fk_pedido_detalle` (`pedi_id`),
  ADD KEY `fk_producto_detalle_pedido` (`prod_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`pedi_id`),
  ADD KEY `fk_usuario_pedido` (`usu_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`prod_id`),
  ADD KEY `fk_categoria_producto` (`catg_id`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`serv_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usu_id`),
  ADD UNIQUE KEY `usu_correo` (`usu_correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `carritos`
--
ALTER TABLE `carritos`
  MODIFY `carr_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del carrito';

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `catg_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID de categoría';

--
-- AUTO_INCREMENT de la tabla `detalle_carrito`
--
ALTER TABLE `detalle_carrito`
  MODIFY `detcarr_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del detalle';

--
-- AUTO_INCREMENT de la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  MODIFY `detpedi_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del detalle';

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `pedi_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del pedido';

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `prod_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del producto';

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `serv_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del servicio';

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `usu_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID único del usuario', AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `carritos`
--
ALTER TABLE `carritos`
  ADD CONSTRAINT `fk_usuario_carrito` FOREIGN KEY (`usu_id`) REFERENCES `usuarios` (`usu_id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `detalle_carrito`
--
ALTER TABLE `detalle_carrito`
  ADD CONSTRAINT `fk_carrito_detalle` FOREIGN KEY (`carr_id`) REFERENCES `carritos` (`carr_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_producto_detalle_carrito` FOREIGN KEY (`prod_id`) REFERENCES `productos` (`prod_id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `detalle_pedido`
--
ALTER TABLE `detalle_pedido`
  ADD CONSTRAINT `fk_pedido_detalle` FOREIGN KEY (`pedi_id`) REFERENCES `pedidos` (`pedi_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_producto_detalle_pedido` FOREIGN KEY (`prod_id`) REFERENCES `productos` (`prod_id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `fk_usuario_pedido` FOREIGN KEY (`usu_id`) REFERENCES `usuarios` (`usu_id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_categoria_producto` FOREIGN KEY (`catg_id`) REFERENCES `categorias` (`catg_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
