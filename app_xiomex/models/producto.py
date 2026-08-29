from django.db import models

from .categoria import Categoria


class Producto(models.Model):

    prod_id = models.AutoField(
        primary_key=True
    )

    prod_nombre = models.CharField(
        max_length=100
    )

    prod_descripcion = models.TextField(
        blank=True,
        null=True
    )

    prod_precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    prod_stock = models.PositiveIntegerField(
        default=0
    )

    prod_img = models.ImageField(
        upload_to="productos/",
        blank=True,
        null=True
    )

    prod_estado = models.CharField(
        max_length=20,
        default="activo"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        db_column="catg_id",
        related_name="productos",
        blank=True,
        null=True
    )

    class Meta:
        db_table = "PRODUCTOS"

    def __str__(self):
        return self.prod_nombre