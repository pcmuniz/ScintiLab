from django.db import models
import vonage

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

class ClientData(models.Model):
    client_name = models.CharField(max_length=30, null=False)
    client_cpf_cnpj = models.CharField(max_length=20, null=False)
    client_rg_ie = models.CharField(max_length=15, null=False)
    client_birthdate = models.DateField(null=False)
    client_email = models.CharField(max_length=30, null=False)
    client_cellphone = models.CharField(max_length=11, null=False)
    client_telephone = models.CharField(max_length=11, null=False)
    client_adress = models.CharField(max_length=60, null=False)
    client_neighborhood = models.CharField(max_length=20, null=False)
    client_zip = models.CharField(max_length=9, null=False)
    client_city = models.CharField(max_length=20, null=False)
    client_state = models.CharField(max_length=2, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.client_name


class BuyerData(models.Model):
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


class PurchaseData(models.Model):
    nome_loja = models.CharField(max_length=30, null=False)
    num_nf = models.CharField(max_length=44, null=False)
    data_compra = models.DateField(null=False)
    cod_produto = models.CharField(max_length=30, null=False)
    valor = models.CharField(max_length=8, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.nome_loja

class EquipmentData(models.Model):
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

class ServiceOrder(models.Model):
    client_data = models.ForeignKey(ClientData, on_delete = models.CASCADE)
    buyer_data = models.ForeignKey(BuyerData, on_delete = models.CASCADE)
    purchase_data = models.ForeignKey(PurchaseData, on_delete = models.CASCADE)
    equipment_data = models.ForeignKey(EquipmentData, on_delete = models.CASCADE)
    protocol_code = models.CharField(max_length=12, null=False)
    create_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, default = 'Recebida')
    is_finished = models.BooleanField(default=False)

    # NOTE: provavelmente remover as opções Recebida e Cancelada
    STATUS_CHOICES = [
        ('Recebida', 'Recebida'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]

    def _str_(self):
        return self.id
    
    def sms(self, *args, **kwargs):
        
        if self.is_finished == True:
            client = vonage.Client(key="4cb174e8", secret="nEngy8sUfWAIFo5d")
            sms = vonage.Sms(client)

            numero_cliente = self.dados_cliente.celular_cliente

            responseData = sms.send_message(
            {
                "from": "Eceel-Tec",
                "to": numero_cliente,
                "text": "Sua ordem de serviço foi concluída!",
            }
            )   

            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        