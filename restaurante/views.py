from django.shortcuts import render
from rest_framework import generics
from .models import ItemMenu, Pedido
from .serializers import ItemMenuSerializer, PedidoSerializer

class ItemMenuList(generics.ListCreateAPIView):
    queryset = ItemMenu.objects.all()
    serializer_class = ItemMenuSerializer

class PedidoCreate(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer