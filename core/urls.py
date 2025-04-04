from django.contrib import admin
from django.urls import path
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    
     # CRUD produtos
    path('', ProdutoListView.as_view(), name='produtos-lista' ),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/update/<int:pk>', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produto/delete/<int:pk>', ProdutoDeleteView.as_view(), name='produto-delete'),
    
    # URLS de login e Logout
    path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)