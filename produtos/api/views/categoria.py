from rest_framework import viewsets
from produtos.models import Categoria
from produtos.api.serializers.categoria import CategoriaSerializer

class CategoriaViewSet (viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
