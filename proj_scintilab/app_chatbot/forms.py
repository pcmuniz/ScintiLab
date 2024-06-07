from django import forms
from .models import CustomerData, OrdemServico

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
        model = OrdemServico
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=OrdemServico.STATUS_CHOICES)
        }

class CreateServiceOrder(forms.Form):
    nome_comprador = forms.CharField(label="Nome Completo", max_length=30, required=True)
    cpf_cnpj = forms.CharField(label="CPF ou CNPJ", max_length=20, required=True)
    rg_ie = forms.CharField(label="RG ou IE", max_length=15, required=True)
    data_nascimento_comprador = forms.DateField(label="Data de Nascimento", required=True)
    email_comprador = forms.CharField(label="Email", max_length=30, required=True)
    celular_comprador = forms.CharField(label="Celular", max_length=11, required=True)
    telefone_comprador = forms.CharField(label="Telefone Fixo", max_length=11, required=True)
    endereco_comprador = forms.CharField(label="Endereço", max_length=60, required=True)
    bairro_comprador = forms.CharField(label="Bairro", max_length=20, required=True)
    cep_comprador = forms.CharField(label="CEP", max_length=9, required=True)
    cidade_comprador = forms.CharField(label="Cidade", max_length=20, required=True)
    uf_comprador = forms.CharField(label="UF", max_length=2, required=True)
