from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClienteCreateView.as_view(), name='pedidos'),
    path('add/',  views.comida , name='add-comida'),
    path('cliente/',  views.ClienteListView.as_view() , name='cliente')
]