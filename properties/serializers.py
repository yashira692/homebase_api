from rest_framework import serializers
from .models import Owner, Property

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "nombre", "documento"]


class PropertySerializer(serializers.ModelSerializer):
    # Campo adicional personalizado que muestra datos del propietario (punto extra)
    propietario_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "titulo",
            "direccion",
            "precio",
            "tipo",
            "propietario",
            "propietario_info",
        ]

    def get_propietario_info(self, obj):
        owner = obj.propietario
        return {
            "id": owner.id,
            "nombre": owner.nombre,
            "documento": owner.documento,
        }
