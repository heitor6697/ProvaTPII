from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Cliente
from .models import Conta
from .models import Transacao
from .forms import form_cadastrar_cliente
from .forms import form_gerar_transacao
from random import seed
from random import randint

# Create your views here.
def index(request):
    contas = Conta.objects.all()
    return render(request, 'Cliente/exibe_contas.html',{'contas':contas})

def cadastra_cliente(request):
    #identifica se é uma requisição POST
    if request.method == 'POST':
        form = form_cadastrar_cliente(request.POST)
        #verifica se o form foi validado
        if form.is_valid():
            nome = form.cleaned_data.get("nome_cliente")
            cpf = form.cleaned_data.get("cpf")
            nascimento = form.cleaned_data.get("nascimento")
            cliente = Cliente(nome=nome, cpf=cpf, nascimento=nascimento)
            cliente.save()
            #gera um numero aleatorio pra conta, apenas para propositos de teste
            numero_da_conta = randint(10000,99999)
            conta = Conta(cliente=cliente, numero=numero_da_conta, limite=200, saldo=500)
            conta.save()
            sucesso = 1
            return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
    #se nao form uma requisicao post, instancia sem request
    else:
        form = form_cadastrar_cliente()
    return render(request,'Cliente/cadastra_cliente.html', {'form':form})

def efetua_transacao(request):
    #recupera o numero da conta
    numero = request.GET.get('numero-conta')
    conta = Conta.objects.get(numero=numero)
    #return HttpResponse(numero)
    #identifica se é uma requisição POST
    if request.method == 'POST':
        #instancia o form como POST request
        form = form_gerar_transacao(request.POST)
        #usa o numero da conta da requisicao HTML para filtrar a conta com esse numero
        #conta = Conta.objects.get(numero=numero)
        saldo = conta.saldo
        limite = conta.limite
        #verifica se o form foi validado
        if form.is_valid():
            
            tipo_transacao = form.cleaned_data.get("tipo")
            valor = form.cleaned_data.get("valor")
            #se é uma transacao de debito:
            if tipo_transacao == "D":
                #se o cliente tem saldo
                if saldo >= valor:
                    novo_saldo = saldo - valor
                    conta.saldo = novo_saldo
                    conta.save()
                    transacao = Transacao(cliente=conta.cliente, conta=conta,
                    tipo=tipo_transacao, valor=valor)
                    transacao.save()    
                    sucesso = 1
                    return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
                #se o cliente nao tem saldo mas o cheque especial cobre
                elif saldo < valor and saldo + limite >= valor:
                    dif = saldo - valor
                    novo_limite = limite + dif
                    conta.saldo = 0
                    conta.limite = novo_limite
                    transacao = Transacao(cliente=conta.cliente, conta=conta,
                    tipo=tipo_transacao, valor=valor)
                    transacao.save()
                    conta.save()
                    sucesso = 1
                    return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
                #se o cliente não tem saldo nem o cheque especial cobre    
                else:
                    sucesso = 0
                    return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
            else:
                #se o cliente deve o cheque especial, paga ele primeiro
                if limite < 200:
                    novo_limite = limite + valor
                    #se o deposito quitar o cheque especial
                    if novo_limite > 200:
                        #retira o excedente do cheque especial
                        limite_excedente = novo_limite - 200
                        #seta o novo limite para 200
                        novo_limite = 200
                        #seta o novo saldo com o limite excedente
                        novo_saldo = saldo + limite_excedente
                        conta.saldo = novo_saldo
                        conta.limite = novo_limite
                        transacao = Transacao(cliente=conta.cliente, conta=conta,
                        tipo=tipo_transacao, valor=valor)
                        transacao.save()
                        conta.save()
                        sucesso = 1
                        return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
                    #continua caso o deposito nao quitar o cheque especial
                    conta.limite = novo_limite
                    transacao = Transacao(cliente=conta.cliente, conta=conta,
                    tipo=tipo_transacao, valor=valor)
                    transacao.save()
                    conta.save()
                    sucesso = 1
                    return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
                #se o cliente não deve o cheque especial, paga o saldo
                else:
                    novo_saldo = saldo + valor
                    conta.saldo = novo_saldo
                    transacao = Transacao(cliente=conta.cliente, conta=conta,
                    tipo=tipo_transacao, valor=valor)
                    transacao.save()
                    conta.save()
                    sucesso = 1
                    return render (request, 'Cliente/fim_operacao.html', {'sucesso':sucesso})
    #se nao for uma requisicao post, instancia sem request            
    else:
        form = form_gerar_transacao()
    return render(request, 'Cliente/cadastra_transacao.html', {'form':form})

def gera_extrato(request):
    #deve pegar a conta do cliente 
    #e buscar todas as transações com o valor da conta
    numero = request.GET.get('numero-conta')
    conta = Conta.objects.get(numero=numero)
    transacoes = Transacao.objects.filter(conta=conta)
    return render(request, 'Cliente/exibe_extrato.html', {'transacoes':transacoes,'conta':conta})

        
        

                        


                    

                    
    



        