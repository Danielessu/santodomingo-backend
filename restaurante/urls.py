from django.urls import path
from .views import ItemMenuList, PedidoCreate, AuthorsView, WelcomeView

urlpatterns = [
    path('menu/', ItemMenuList.as_view(), name='menu-list'),
    path('pedidos/', PedidoCreate.as_view(), name='pedido-create'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
]