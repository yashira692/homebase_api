from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .models import Owner, Property
from .serializers import OwnerSerializer, PropertySerializer

class OwnerViewSet(viewsets.ModelViewSet):
    """CRUD completo para propietarios: GET, POST, PUT, PATCH, DELETE"""
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [AllowAny]


class PropertyViewSet(viewsets.ModelViewSet):
    """CRUD para propiedades + búsqueda por `titulo` o `tipo` usando ?search="""
    # select_related para evitar consultas N+1 al mostrar propietario
    queryset = Property.objects.select_related("propietario").all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["titulo", "tipo"]
