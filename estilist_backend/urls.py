from django.urls import path, include
from rest_framework import routers
from estilist_backend.views import CrearUsuario, UsuariosViewSet, CrearSuperUsuario

router = routers.DefaultRouter()    
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crear-usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('crear-superusuario/', CrearSuperUsuario.as_view(), name='crear_superusuario'),
]