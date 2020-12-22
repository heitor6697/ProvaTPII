# ProvaTPII
<h1>Prova de Tópicos de Informação</h1>

Este mini-sistema implementado através do Django, baseado em Python, foi feito como avaliação para a disciplina de Tópicos Especiais II em Sistemas de Informação.
Ele possui um banco de dados com três diferentes tabelas: Cliente, Conta e Transação. Cada clinte está associado à somente uma conta, e cada conta está associada a (n) transações.
<h4>Possui as seguintes funcionalidades:</h4>
</br>
<h5>Cadastrar Cliente:</h5> Recebe o Nome, CPF e Data de Nascimento. Quando o cliente é cadastrado, uma conta é aberta para ele automaticamente. Não existe validação de CPF, e os numeros de conta são gerados aleatoriamente.
Não existe validação quanto à unicidade de cada conta, sendo apenas de caráter demonstrativo. Cada cliente começa com um saldo de 500 reais e um limite de cheque especial
de 200 reais.
</br>
<h5>Efetuar Transação:</h5> Recebe o tipo de transação e o valor. Transações de débito acima do saldo descontarão do cheque especial caso o limite não seja estourado.
Caso o valor da transação seja maior que a soma do limite do cheque especial e o saldo, o sistema recusa a transação. As transações de crédito irão sempre primeiro quitar o cheque
especial.
<h5>Gerar Extrato:</h5> Gera o extrato de determinado cliente, mostrando quais as transações foram efetuadas, qual o saldo e qual o limite disponível para o cheque especial.



/upload/main
