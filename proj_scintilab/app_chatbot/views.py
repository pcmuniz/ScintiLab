from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import CustomerLoginForm, CustomerRegisterForm, IndividualForm, CompanyForm, PersonTypeForm, ChangeOrderStatusForm
from .models import CustomerData, DadosCliente, DadosCompra, DadosComprador, DadosEquipamento, EmployeeData, OrdemServico
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password

class HomePage(View):
    def get(self, request):
        return render(request, 'app_chatbot/HomePage.html')
    
class CustomerPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/CustomerPage.html')
    
class CustomerLoginPage(View):
    def get(self, request):
        form = CustomerLoginForm()
        return render(request, 'app_chatbot/CustomerLoginPage.html', {'form' : form})
    # def post(self, request):
    #     form = CustomerLoginForm(request.POST)

    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
            
    #         user = authenticate(username=email, password=password)
            
    #         if user is None:
    #             form.add_error(None, 'Invalid email or password')  # Add a non-field error
    #             return render(request, 'app_chatbot/CustomerLoginPage.html', {'form': form})
            
    #         auth_login(request, user)
    #         return redirect('customer-page')
        
    #     # If form is invalid, render the login page with the form and errors
    #     return render(request, 'app_chatbot/CustomerLoginPage.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomerData.objects.get(email=email)
        except CustomerData.DoesNotExist:
            user = None
            print(user)
        if user is not None and check_password(password, user.password):
            return redirect('/cliente')
        else:
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'app_chatbot/CustomerLoginPage.html', {'error_message': error_message})

class EmployeeLoginPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/EmployeeLoginPage.html')
    
class CustomerRegisterPage(View):
    def get(self, request):
        form = CustomerRegisterForm()
        return render(request, 'app_chatbot/CustomerRegisterPage.html', {'form' : form})
    
    def post(self, request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-login-page')

        return render(request, 'app_chatbot/CustomerRegisterPage.html', {'form': form})
    
class EmployeeRegisterPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/EmployeeRegisterPage.html')
    
    def post(self, request):
        if request.method == "POST":
            form = request.POST
            code = form.get("code")
            email = form.get("email")

            if EmployeeData.objects.filter(code=code).exists() or EmployeeData.objects.filter(email=email).exists():
                return HttpResponse("Dados já cadastrados.", status=400)
            
            else:
                employee_data = EmployeeData(
                    code = form["code"],
                    email = form["email"],
                    name = form["code"],
                    surname = form["code"],
                    password = form["code"]
                )
                employee_data.save()

        return render(request, 'app_chatbot/EmployeeRegisterPage.html')



class OrdemServicoView(View):
    def get(self, request):
        return render(request, 'app_chatbot/os.html')
    
    def post(self, request):
        if request.method == "POST":
            form = request.POST
            dados_cliente = DadosCliente(
                nome_cliente=form["nome_cliente"], cpf_cnpj =form["id_cliente"], rg_ie=form["sub_id_cliente"], data_nascimento_cliente=form["data_nascimento_cliente"],
                email_cliente=form["email_cliente"], celular_cliente=form["celular_cliente"], telefone_cliente=form["telefone_cliente"], endereco_cliente=form["endereco_cliente"],
                bairro_cliente=form["bairro_cliente"], cep_cliente=form["cep_cliente"], cidade_cliente=form["cidade_cliente"], uf_cliente=form["uf_cliente"]
                )
            dados_cliente.save()

            dados_comprador = DadosComprador(
                nome_comprador=form["nome_comprador"], cpf_cnpj =form["id_comprador"], rg_ie=form["sub_id_comprador"], data_nascimento_comprador=form["data_nascimento_comprador"],
                email_comprador=form["email_comprador"], celular_comprador=form["celular_comprador"], telefone_comprador=form["telefone_comprador"], endereco_comprador=form["endereco_comprador"],
                bairro_comprador=form["bairro_comprador"], cep_comprador=form["cep_comprador"], cidade_comprador=form["cidade_comprador"], uf_comprador=form["uf_comprador"]
                )
            dados_comprador.save()

            dados_compra = DadosCompra(
                nome_loja =form["loja"], num_nf=form["nf"], data_compra=form["data_compra"],
                cod_produto=form["cod_produto"], valor=form["valor"]
                )
            dados_compra.save()

            dados_equipamento = DadosEquipamento(
                nome_equipamento=form["equipamento"], marca =form["marca"], lacrado=form["estado_lacre"], modelo=form["modelo"],
                num_serie=form["num_serie"], senha_usuario=form["senha_usuario"], defeito=form["texto_defeito"], estado=form["estado_aparelho"],
                acessorios=form["acessorios"], observacoes=form["observacoes"], arquivos=form["arquivos"]
                )
            dados_equipamento.save()


        return render(request, 'app_chatbot/os.html')

class OrdemServicoAtivaView(View):
    def get(self, request):
        nomes = DadosCliente.objects.values('id', 'nome_cliente')
        eletrodomesticos = DadosEquipamento.objects.values('nome_equipamento')
        problemas = DadosEquipamento.objects.values('defeito')

        contexto = {
            'nomes': nomes,
            'eletrodomesticos': eletrodomesticos,
            'problemas': problemas,
        }

        return render(request, 'app_chatbot/os_ativas.html', contexto)

    
class ChangeOrderStatus(View):
    def get(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        form = ChangeOrderStatusForm(instance=ordem_servico)
        return render(request, 'app_chatbot/TemporaryPages/ChangeOrderStatus/change_order_status.html', {'form': form, 'ordem_servico': ordem_servico})

    def post(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        form = ChangeOrderStatusForm(request.POST, instance=ordem_servico)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirecione para uma página de sucesso após a alteração
        return render(request, 'app_chatbot/TemporaryPages/ChangeOrderStatus/change_order_status.html', {'form': form, 'ordem_servico': ordem_servico})

def registration_view(request):
    form = None
    form_type = None
    
    if request.method == 'POST':
        person_type_form = PersonTypeForm(request.POST)
        if person_type_form.is_valid():
            person_type = person_type_form.cleaned_data['person_type']
            if person_type == 'individual':
                form = IndividualForm(request.POST)
                form_type = 'individual'
            else:
                form = CompanyForm(request.POST)
                form_type = 'company'
            
            if form.is_valid():
                form.save()
                return redirect('registration_success')
    else:
        person_type_form = PersonTypeForm()
    
    return render(request, 'app_chatbot/TemporaryPages/CPFxCNPJ/registration.html', {
        'person_type_form': person_type_form,
        'form': form,
        'form_type': form_type,
    })