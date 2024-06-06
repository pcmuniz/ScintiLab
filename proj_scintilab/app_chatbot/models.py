from django.db import models


# class Person(models.Model):
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)

#     class Meta:
#         abstract = True

# class IndividualData(Person):
#     full_name = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=11, unique=True)

#     def __str__(self):
#         return self.full_name

# class CompanyData(Person):
#     company_name = models.CharField(max_length=100)
#     cnpj = models.CharField(max_length=14, unique=True)

#     def __str__(self):
#         return self.company_name

class CustomerData(models.Model):
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, null=False)
    cellphone = models.IntegerField(null=False)
    
class EmployeeData(models.Model):
    code = models.IntegerField(null=False)
    email = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)

class DadosCliente(models.Model):
    nome_cliente = models.CharField(max_length=30, null=False)
    cpf_cnpj = models.CharField(max_length=20, null=False)
    rg_ie = models.CharField(max_length=15, null=False)
    data_nascimento_cliente = models.DateField(null=False)
    email_cliente = models.CharField(max_length=30, null=False)
    celular_cliente = models.CharField(max_length=11, null=False)
    telefone_cliente = models.CharField(max_length=11, null=False)
    endereco_cliente = models.CharField(max_length=60, null=False)
    bairro_cliente = models.CharField(max_length=20, null=False)
    cep_cliente = models.CharField(max_length=9, null=False)
    cidade_cliente = models.CharField(max_length=20, null=False)
    uf_cliente = models.CharField(max_length=2, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.nome_cliente


class DadosComprador(models.Model):
    nome_comprador = models.CharField(max_length=30, null=False)
    cpf_cnpj = models.CharField(max_length=20, null=False)
    rg_ie = models.CharField(max_length=15, null=False)
    data_nascimento_comprador = models.DateField(null=False)
    email_comprador = models.CharField(max_length=30, null=False)
    celular_comprador = models.CharField(max_length=11, null=False)
    telefone_comprador = models.CharField(max_length=11, null=False)
    endereco_comprador = models.CharField(max_length=60, null=False)
    bairro_comprador = models.CharField(max_length=20, null=False)
    cep_comprador = models.CharField(max_length=9, null=False)
    cidade_comprador = models.CharField(max_length=20, null=False)
    uf_comprador = models.CharField(max_length=2, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.nome_comprador


class DadosCompra(models.Model):
    nome_loja = models.CharField(max_length=30, null=False)
    num_nf = models.CharField(max_length=44, null=False)
    data_compra = models.DateField(null=False)
    cod_produto = models.CharField(max_length=30, null=False)
    valor = models.CharField(max_length=8, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.nome_loja

class DadosEquipamento(models.Model):
    nome_equipamento = models.CharField(max_length=30, null=False)
    marca = models.CharField(max_length=20, null=False)
    lacrado = models.CharField(max_length=3, null=False)
    modelo = models.CharField(max_length=15, null=False)
    num_serie = models.CharField(max_length=30, null=False)
    senha_usuario = models.CharField(max_length=11, null=False)
    defeito = models.CharField(max_length=300, null=False)
    estado = models.CharField(max_length=300, null=False)
    acessorios = models.CharField(max_length=300, null=False)
    observacoes = models.CharField(max_length=300, null=False)
    arquivos = models.CharField(max_length=300, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.nome_equipamento

class OrdemServico(models.Model):
    dados_cliente = models.ForeignKey(DadosCliente, on_delete = models.CASCADE)
    dados_comprador = models.ForeignKey(DadosComprador, on_delete = models.CASCADE)
    dados_compra = models.ForeignKey(DadosCompra, on_delete = models.CASCADE)
    dados_equipamento = models.ForeignKey(DadosEquipamento, on_delete = models.CASCADE)
    protocolo = models.CharField(max_length=12, null=False)
    data_criacao = models.DateField(null = False)
    status = models.CharField(max_length=15, default = 'Recebida')
    STATUS_CHOICES = [
        ('Recebida', 'Recebida'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]

    def _str_(self):
        return self.id
