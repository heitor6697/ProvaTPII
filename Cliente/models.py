from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    nascimento = models.DateField()
    objects = models.Manager()
    def __str__(self):
        return self.nome

class Conta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE,primary_key=False)
    numero = models.IntegerField()
    limite = models.FloatField()
    saldo = models.FloatField()
    objects = models.Manager()
    def __str__(self):
        return str(self.numero)

class Transacao(models.Model):
    TIPO_TRANSACAO_CHOICES = (("D", "Débito"),("C", "Crédito"),)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_TRANSACAO_CHOICES, blank=False, null=False)
    valor = models.FloatField()
    objects = models.Manager()

