from rest_framework import viewsets
from .models import Usuarios
from .serializers import UsuariosSerializer, AuthUserSerialize
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User as auth


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class AuthUserViewSet (viewsets.ModelViewSet):
    queryset = auth.objects.all()
    serializer_class = AuthUserSerialize

class CreateUser(View):
    def post(self, request):
        # Leer el JSON del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        password = data.get('contrasena')
        email = data.get('correo')
        username = email
    
        # Intenta crear el objeto de Usuarios
        try:
            usuario_personalizado = Usuarios(
                nombre=data.get('nombre'),
                apellidopaterno=data.get('apellidopaterno'),
                apellidomaterno=data.get('apellidomaterno'),
                correo=email,
                edad=data.get('edad'),
                genero=data.get('genero'),
                pais=data.get('pais'),
                fecharegistro=data.get('fecharegistro'),
                estado=True
            )
        except Exception as e:
            return HttpResponse(f'Error al crear el objeto Usuarios: {str(e)}', status=400)
        
        try:
            usuario_personalizado.save()
        except Exception as e:
            return HttpResponse(f'Error al crear el usuario personalizado: {str(e)}', status=400)

        try:
            usuario_auth = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            usuario_personalizado.idlogin = usuario_auth
            usuario_personalizado.save()  

            return JsonResponse({'idUsuario': usuario_personalizado.idusuario}, status=201)
        except Exception as e:
            try:
                usuario_personalizado.delete()  
            except Exception as delete_exception:
                return HttpResponse(f'Error al eliminar el usuario personalizado: {str(delete_exception)}', status=500)

            return HttpResponse(f'Error al crear el usuario de autenticación: {str(e)} {username}', status=400)
        
class CrearSuperUsuario(View):
    def post(self, request):
        # Leer el JSON del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username:
            return JsonResponse({'error': 'The given username must be set'}, status=400)

        # Crea el usuario
        usuario_auth = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # Crea el objeto de Usuarios y relaciona
        usuario_personalizado = Usuarios.objects.create(
            idlogin=usuario_auth,
            nombre=data.get('nombre'),
            apellidopaterno=data.get('apellidopaterno'),
            apellidomaterno=data.get('apellidomaterno'),
            correo=email,
            edad=data.get('edad'),
            genero=data.get('genero'),
            tiporostro=data.get('tiporostro'),
            tipocuerpo=data.get('tipocuerpo'),
            fecharegistro=data.get('fecharegistro'),
            estado=True
        )

        return JsonResponse({'message': 'Usuario creado con éxito'}, status=201)
