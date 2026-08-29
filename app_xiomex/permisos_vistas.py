from django.shortcuts import redirect


def usuario_autenticado(request):
    return "usuario_id" in request.session


def es_administrador(request):
    return (
        request.session.get("usuario_rol")
        in ["administrador", "superadministrador"]
    )


def es_superadministrador(request):
    return (
        request.session.get("usuario_rol")
        == "superadministrador"
    )


def requerir_administrador(request):
    if not usuario_autenticado(request):
        return redirect("/auth/")

    if not es_administrador(request):
        return redirect("/perfil/")

    return None


def requerir_superadministrador(request):
    if not usuario_autenticado(request):
        return redirect("/auth/")

    if not es_superadministrador(request):
        return redirect("/perfil/")

    return None