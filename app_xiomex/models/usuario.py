from django.db import models


class Usuario(models.Model):

    usu_id = models.AutoField(
        primary_key=True
    )

    usu_nombre = models.CharField(
        max_length=50
    )

    usu_apellido = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    usu_rol = models.CharField(
        max_length=20,
        default="cliente"
    )
    
    usu_superadmin_original = models.BooleanField(
        default=False
    )

    usu_telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    usu_correo = models.EmailField(
        unique=True,
        max_length=100
    )

    usu_contraseña = models.CharField(
        max_length=255
    )

    usu_img = models.ImageField(
        upload_to="perfiles/",
        default="default_perfil.png"
    )

    class Meta:

        db_table = "USUARIOS"

    def __str__(self):

        return self.usu_correo
