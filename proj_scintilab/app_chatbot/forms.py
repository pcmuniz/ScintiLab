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
