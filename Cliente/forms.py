from django import forms
from Cliente.models import Cliente
from Cliente.models import Conta
from Cliente.models import Transacao

class form_cadastrar_cliente(forms.Form):
    nome_cliente = forms.CharField(label='Nome do Cliente', max_length=200)
    cpf = forms.IntegerField(label='CPF do Cliente')
    nascimento = forms.DateField(label='Data de Nascimento do Cliente', input_formats=['%d/%m/%Y'])

class form_criar_conta(forms.Form):
    #cpf_cliente = forms.CharField(label='Nome do Cliente', max_length=200, widget=forms.HiddenInput())
    numero_conta = forms.IntegerField(label='Numero da Conta')
    limite = forms.FloatField(label='Limite do Cheque Especial')
    saldo = forms.FloatField(label='Saldo Inicial')

class form_gerar_transacao(forms.Form):
    TIPO_TRANSACAO_CHOICES = (("D", "Débito"),("C", "Crédito"),)
    #numero_conta = forms.IntegerField(widget=forms.HiddenInput())
    #nome_cliente = forms.CharField( widget=forms.HiddenInput())
    tipo = forms.ChoiceField(label='Tipo de Transação', choices=TIPO_TRANSACAO_CHOICES)
    valor = forms.FloatField(label='Valor da Transação')

class form_busca_cliente(forms.Form):
    cpf_cliente = forms.IntegerField(label='Digite o CPF do cliente para Busca')
