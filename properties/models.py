from django.db import models

class Owner(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


class Property(models.Model):
    TIPOS = (
        ("casa", "Casa"),
        ("departamento", "Departamento"),
        ("otro", "Otro"),
    )
    titulo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    propietario = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="propiedades")

    def __str__(self):
        return f"{self.titulo} — {self.direccion}"
