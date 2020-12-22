from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro',views.cadastra_cliente, name='cadastro'),
    path('transacao',views.efetua_transacao, name='transacao'),
    path('extrato',views.gera_extrato, name='extrato')
]
