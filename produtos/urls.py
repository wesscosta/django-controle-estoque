from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos.api.views import avaliacao, categoria, fornecedor, produto, usuario
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView


router = DefaultRouter()
router.register(r'fornecedores', fornecedor.FornecedorViewSet)
router.register(r'categorias', categoria.CategoriaViewSet)
router.register(r'produtos', produto.ProdutoViewSet)
router.register(r'avaliacoes', avaliacao.AvaliacaoViewSet)
router.register(r'usuarios', usuario.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('me/', usuario.MeView.as_view(), name='me'),
    
    path('', ProdutoListView.as_view(), name='produtos-lista' ),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/update/<int:pk>', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produto/delete/<int:pk>', ProdutoDeleteView.as_view(), name='produto-delete'),
    
]
