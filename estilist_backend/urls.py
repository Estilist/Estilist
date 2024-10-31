from django.urls import path, include
from rest_framework import routers
from estilist_backend.views import CreateUser, UsuariosViewSet, CrearSuperUsuario, AuthUserViewSet

router = routers.DefaultRouter()    
router.register(r'usuarios', UsuariosViewSet)
router.register(r'auth', AuthUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crear-usuario/', CreateUser.as_view(), name='crear_usuario'),
    path('crear-superusuario/', CrearSuperUsuario.as_view(), name='crear_superusuario'),
]