from rest_framework import viewsets
from .models import Usuarios
from .serializers import UsuariosSerializer

# Create your views here.
class  UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer