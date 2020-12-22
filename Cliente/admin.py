from django.contrib import admin
from .models import Cliente
from .models import Conta
from .models import Transacao
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Transacao)
