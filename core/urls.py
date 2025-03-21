from django.contrib import admin
from django.urls import path
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoListView.as_view(), name='produtos-lista' ),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/update/<int:pk>', ProdutoUpdateView.as_view(), name='produto-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)