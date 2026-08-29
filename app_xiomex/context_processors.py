from .models.usuario import Usuario

def usuario_actual(request):
    if "usuario_id" not in request.session:
        return {"usuario": None}

    usuario = Usuario.objects.filter(usu_id=request.session["usuario_id"]).first()

    return {"usuario": usuario}