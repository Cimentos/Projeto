from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, UserViewSet, login_view
from . import views
from .views import pagina_login

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view),
    path('pagina-login/', pagina_login, name='pagina_login'), 
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pagina-produtos/', views.produtos, name='produtos'),  # <-- página HTML
    path('index/', views.index, name='index'),
]