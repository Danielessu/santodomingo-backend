from rest_framework import serializers
from .models import ItemMenu, Pedido

class ItemMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = ['id', 'categoria', 'nombre', 'descripcion', 'precio', 'imagen']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['nombre', 'telefono', 'direccion', 'total']