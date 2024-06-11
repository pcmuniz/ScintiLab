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

class ClientData(models.Model):
    client_name = models.CharField(max_length=30, null=False)
    client_cpf_cnpj = models.CharField(max_length=20, null=False)
    client_rg_ie = models.CharField(max_length=15, null=False)
    client_birthdate = models.DateField(null=False)
    client_email = models.CharField(max_length=30, null=False)
    client_cellphone = models.CharField(max_length=13, null=False)
    client_telephone = models.CharField(max_length=11, null=False)
    client_adress = models.CharField(max_length=60, null=False)
    client_neighborhood = models.CharField(max_length=20, null=False)
    client_zip = models.CharField(max_length=9, null=False)
    client_city = models.CharField(max_length=20, null=False)
    client_state = models.CharField(max_length=2, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.client_name


class BuyerData(models.Model):
    buyer_name = models.CharField(max_length=30, null=False)
    buyer_cpf_cnpj = models.CharField(max_length=20, null=False)
    buyer_rg_ie = models.CharField(max_length=15, null=False)
    buyer_birthdate = models.DateField(null=False)
    buyer_email = models.CharField(max_length=30, null=False)
    buyer_cellphone = models.CharField(max_length=11, null=False)
    buyer_telephone = models.CharField(max_length=11, null=False)
    buyer_adress = models.CharField(max_length=60, null=False)
    buyer_neighborhood = models.CharField(max_length=20, null=False)
    buyer_zip = models.CharField(max_length=9, null=False)
    buyer_city = models.CharField(max_length=20, null=False)
    buyer_state = models.CharField(max_length=2, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.buyer_name


class PurchaseData(models.Model):
    store_name = models.CharField(max_length=30, null=False)
    receipt_number = models.CharField(max_length=44, null=False)
    purchase_date = models.DateField(null=False)
    product_code = models.CharField(max_length=30, null=False)
    price = models.CharField(max_length=8, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.store_name

class EquipmentData(models.Model):
    equipment_name = models.CharField(max_length=30, null=False)
    brand = models.CharField(max_length=20, null=False)
    new = models.CharField(max_length=3, null=False)
    model = models.CharField(max_length=15, null=False)
    serial_number = models.CharField(max_length=30, null=False)
    user_password = models.CharField(max_length=11, null=False)
    defect = models.CharField(max_length=300, null=False)
    state = models.CharField(max_length=300, null=False)
    acessories = models.CharField(max_length=300, null=False)
    observations = models.CharField(max_length=300, null=False)
    files = models.CharField(max_length=300, null=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.equipment_name

class ServiceOrder(models.Model):
    client_data = models.ForeignKey(ClientData, on_delete = models.CASCADE)
    buyer_data = models.ForeignKey(BuyerData, on_delete = models.CASCADE)
    purchase_data = models.ForeignKey(PurchaseData, on_delete = models.CASCADE)
    equipment_data = models.ForeignKey(EquipmentData, on_delete = models.CASCADE)
    protocol_code = models.CharField(max_length=8, null=False)
    create_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, default = 'Recebida')
    is_finished = models.BooleanField(default=False)

    @property
    def client_name(self):
        return self.client_data.client_name
    
    @property
    def equipment_name(self):
        return self.equipment_data.equipment_name
    

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
        