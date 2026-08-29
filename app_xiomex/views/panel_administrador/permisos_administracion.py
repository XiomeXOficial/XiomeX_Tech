def puede_administrar(usuario_actual, usuario_objetivo):

    # No puede administrarse a sí mismo
    if usuario_actual.usu_id == usuario_objetivo.usu_id:
        return False

    # Superadministrador original
    if usuario_actual.usu_superadmin_original:
        return True

    # Superadministrador normal
    if usuario_actual.usu_rol == "superadministrador":
        return usuario_objetivo.usu_rol in [
            "administrador",
            "cliente"
        ]

    # Administrador
    if usuario_actual.usu_rol == "administrador":
        return usuario_objetivo.usu_rol == "cliente"

    # Cliente
    return False