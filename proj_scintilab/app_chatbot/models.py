from django.db import models

class OrdemServico(models.Model):
    tipo_cliente = [('1', 'Pessoa Física'), ('2', 'Pessoa Jurídica')]
   