from rest_framework import viewsets
from produtos.models import Fornecedor
from produtos.api.serializers.fornecedor import FornecedorSerializer

class FornecedorViewSet (viewsets.ModelViewSet):
  queryset = Fornecedor.objects.all()
  serializer_class = FornecedorSerializer
