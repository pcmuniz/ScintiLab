from django import forms

from .models import CustomerData

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
