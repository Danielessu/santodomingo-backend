from django.urls import path
from .views import ItemMenuList, PedidoCreate

urlpatterns = [
    path('menu/', ItemMenuList.as_view(), name='menu-list'),
    path('pedidos/', PedidoCreate.as_view(), name='pedido-create'),
]