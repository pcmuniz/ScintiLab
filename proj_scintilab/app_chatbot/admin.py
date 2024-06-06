from django.contrib import admin
from .models import DadosCliente, DadosComprador, DadosCompra, DadosEquipamento, OrdemServico
# , OrdemServico

admin.site.register(DadosCliente)
admin.site.register(DadosComprador)
admin.site.register(DadosCompra)
admin.site.register(DadosEquipamento)
admin.site.register(OrdemServico)
# admin.site.register(OrdemServico)