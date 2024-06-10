from django import forms
from .models import CustomerData, ServiceOrder
from django.core.exceptions import ValidationError

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerData
        fields = ['cellphone', 'email', 'name', 'surname', 'password']
        widgets = {
            'password' : forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomerData.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")
        return email
    
class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = CustomerData
        fields = ['email', 'password']
        widgets = {
            'password' : forms.PasswordInput(),
        }


class IndividualForm(forms.ModelForm):
    class Meta:
        # model = IndividualData
        fields = ['full_name', 'cpf', 'email', 'phone']

class CompanyForm(forms.ModelForm):
    class Meta:
        # model = CompanyData
        fields = ['company_name', 'cpnj', 'email', 'phone']

class PersonTypeForm(forms.Form):
    PERSON_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company'),
    ]
    person_type = forms.ChoiceField(choices=PERSON_TYPE_CHOICES, widget=forms.RadioSelect)

class ChangeOrderStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=ServiceOrder.STATUS_CHOICES)
        }

class CreateServiceOrder(forms.Form):
  
    client_name = forms.CharField(label="Nome Completo", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 1025px;'}))
    client_cpf_cnpj = forms.CharField(label="CPF ou CNPJ", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_rg_ie = forms.CharField(label="RG ou IE", max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_birthdate = forms.DateField(label="Data de Nascimento", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_email = forms.CharField(label="Email", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_cellphone = forms.CharField(label="Celular", max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_telephone = forms.CharField(label="Telefone Fixo", max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    client_adress = forms.CharField(label="Rua", max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 1025px;'}))
    client_neighborhood = forms.CharField(label="Bairro", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    client_zip = forms.CharField(label="CEP", max_length=9, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    client_city = forms.CharField(label="Cidade", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    client_state = forms.CharField(label="UF", max_length=2, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))

    buyer_name = forms.CharField(label="Nome Completo", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 1025px;'}))
    buyer_cpf_cnpj = forms.CharField(label="CPF ou CNPJ", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_rg_ie = forms.CharField(label="RG ou IE", max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_birthdate = forms.DateField(label="Data de Nascimento", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_email = forms.CharField(label="Email", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_cellphone = forms.CharField(label="Celular", max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_telephone = forms.CharField(label="Telefone Fixo", max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    buyer_adress = forms.CharField(label="Rua", max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 1025px;'}))
    buyer_neighborhood = forms.CharField(label="Bairro", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    buyer_zip = forms.CharField(label="CEP", max_length=9, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    buyer_city = forms.CharField(label="Cidade", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    buyer_state = forms.CharField(label="UF", max_length=2, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))

    store_name = forms.CharField(label="Loja", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 1025px;'}))
    receipt_number = forms.CharField(label="Numero da NF", max_length=44, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 480px;'}))
    purchase_date = forms.DateField(label="Data da Compra", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 480px;'}))
    product_code = forms.CharField(label="Código do Produto", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 480px;'}))
    price = forms.CharField(label="Valor (R$)", max_length=9, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 480px;'}))

    equipment_name = forms.CharField(label="Equipamento", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    brand = forms.CharField(label="Marca", max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    new = forms.CharField(label="Lacre Intacto", max_length=3, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    model = forms.CharField(label="Modelo", max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    serial_number = forms.CharField(label="Nº de Série", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    user_password = forms.CharField(label="Senha de Usuário", max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    defect = forms.CharField(label="Defeito Reclamado", max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    state = forms.CharField(label="Estado do Aparelho", max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px;'}))
    acessories = forms.CharField(label="Acessórios", max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    observations = forms.CharField(label="Observações p/ o Técnico", max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    files = forms.CharField(label="Arquivos para Salvar", max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))

    def clean_name(self):
        name = self.cleaned_data['client_name']
        if name == 'CR7':
            raise ValidationError('O nome nao pode ser esse')
        else:
            return name