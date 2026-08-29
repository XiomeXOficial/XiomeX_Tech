from django.db import models


class Categoria(models.Model):

    catg_id = models.AutoField(
        primary_key=True
    )

    catg_nombre = models.CharField(
        max_length=50
    )

    class Meta:
        db_table = "CATEGORIAS"

    def __str__(self):
        return self.catg_nombre