from django.urls import path, include
from rest_framework import routers
from estilist_backend import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls))
]