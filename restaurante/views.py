from django.shortcuts import render
from rest_framework import generics
from .models import ItemMenu, Pedido
from .serializers import ItemMenuSerializer, PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WelcomeView(APIView):
    def get(self, request):
        return Response({"message": "¡Bienvenido al backend de Santo Domingo! API funcionando correctamente."}, status=status.HTTP_200_OK)
    
class AuthorsView(APIView):
    def get(self, request):
        authors = [
            {"Nombre": "Juanita Parra Suárez", "ID": "325708"},
            {"Nombre": "Andrés Camilo Torres Guerrero", "ID": "322926"},
            {"Nombre": "Daniel Felipe Esquinas Suárez", "ID": "287806"},
        ]
        return Response(authors, status=status.HTTP_200_OK)
    
class ItemMenuList(generics.ListCreateAPIView):
    queryset = ItemMenu.objects.all()
    serializer_class = ItemMenuSerializer

class PedidoCreate(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer