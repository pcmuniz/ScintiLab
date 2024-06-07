from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import CustomerLoginForm, CustomerRegisterForm, IndividualForm, CompanyForm, PersonTypeForm, ChangeOrderStatusForm, CreateServiceOrder
from .models import CustomerData, ClientData, PurchaseData, BuyerData, EquipmentData, EmployeeData, ServiceOrder
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password

class HomePage(View):
    def get(self, request):
        return render(request, 'app_chatbot/HomePage.html')
    
class Modal(View):
    def get(self,request):
        return render(request, 'app_chatbot/TemporaryPages/GuideModal/modal.html')

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

# TODO: transformar CancelOrder em função, para ser chamada tanto pelo cliente quanto pelo funcionário
class CancelOrder(View):
    def get(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        return render(request, 'app_chatbot/TemporaryPages/CancelOrder/cancel_order.html', {'ordem_servico': ordem_servico})

    def post(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        if ordem_servico.status != 'Cancelada':
            ordem_servico.status = 'Cancelada'
            ordem_servico.save()
        return redirect('order_detail', order_id=order_id) # TODO: redirect


class ChangeOrderStatus(View):
    def get(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        form = ChangeOrderStatusForm(instance=ordem_servico)
        return render(request, 'app_chatbot/TemporaryPages/ChangeOrderStatus/change_order_status.html', {'form': form, 'ordem_servico': ordem_servico})

    def post(self, request, order_id):
        ordem_servico = get_object_or_404(OrdemServico, id=order_id)
        form = ChangeOrderStatusForm(request.POST, instance=ordem_servico)
        if form.is_valid():
            ordem_servico = form.save(commit = False)
            if ordem_servico.status == 'Concluída':
                ordem_servico.is_finished = True
            form.save()
            ordem_servico.sms()
            return redirect('success_page')  # TODO: redirect
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
                return redirect('registration_success') # TODO: redirect
    else:
        person_type_form = PersonTypeForm()
    
    return render(request, 'app_chatbot/TemporaryPages/CPFxCNPJ/registration.html', {
        'person_type_form': person_type_form,
        'form': form,
        'form_type': form_type,
    })

class Teste(View):
    def get(self, request):
        form = CreateServiceOrder()
        ctx = {'form': form}
        return render(request, 'app_chatbot/teste.html', ctx)
    
    def post(self, request):
        form = CreateServiceOrder(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            client_cpf_cnpj = form.cleaned_data['client_cpf_cnpj']
            client_rg_ie = form.cleaned_data['client_rg_ie']
            client_birthdate = form.cleaned_data['client_birthdate']
            client_email = form.cleaned_data['client_email']
            client_cellphone = form.cleaned_data['client_cellphone']
            client_telephone = form.cleaned_data['client_telephone']
            client_adress = form.cleaned_data['client_adress']
            client_neighborhood = form.cleaned_data['client_neighborhood']
            client_zip = form.cleaned_data['client_zip']
            client_city = form.cleaned_data['client_city']
            client_state = form.cleaned_data['client_state']

            buyer_name = form.cleaned_data['buyer_name']
            buyer_cpf_cnpj = form.cleaned_data['buyer_cpf_cnpj']
            buyer_rg_ie = form.cleaned_data['buyer_rg_ie']
            buyer_birthdate = form.cleaned_data['buyer_birthdate']
            buyer_email = form.cleaned_data['buyer_email']
            buyer_cellphone = form.cleaned_data['buyer_cellphone']
            buyer_telephone = form.cleaned_data['buyer_telephone']
            buyer_adress = form.cleaned_data['buyer_adress']
            buyer_neighborhood = form.cleaned_data['buyer_neighborhood']
            buyer_zip = form.cleaned_data['buyer_zip']
            buyer_city = form.cleaned_data['buyer_city']
            buyer_state = form.cleaned_data['buyer_state']

            store_name = form.cleaned_data['store_name']
            receipt_number = form.cleaned_data['receipt_number']
            purchase_date = form.cleaned_data['purchase_date']
            product_code = form.cleaned_data['product_code']
            price = form.cleaned_data['price']

            equipment_name = form.cleaned_data['equipment_name']
            brand = form.cleaned_data['brand']
            new = form.cleaned_data['new']
            model = form.cleaned_data['model']
            serial_number = form.cleaned_data['serial_number']
            user_password = form.cleaned_data['user_password']
            defect = form.cleaned_data['defect']
            state = form.cleaned_data['state']
            acessories = form.cleaned_data['acessories']
            observations = form.cleaned_data['observations']
            files = form.cleaned_data['files']
    
            buyer_data = BuyerData(buyer_name = buyer_name, buyer_cpf_cnpj = buyer_cpf_cnpj, buyer_rg_ie = buyer_rg_ie,buyer_birthdate = buyer_birthdate,
                buyer_email = buyer_email, buyer_cellphone = buyer_cellphone, buyer_telephone = buyer_telephone, buyer_adress = buyer_adress,
                buyer_neighborhood = buyer_neighborhood,buyer_zip = buyer_zip,buyer_city = buyer_city,buyer_state = buyer_state)
            
            buyer_data.save()

            client_data = ClientData(client_name = client_name, client_cpf_cnpj = client_cpf_cnpj, client_rg_ie = client_rg_ie,client_birthdate = client_birthdate,
                client_email = client_email, client_cellphone = client_cellphone, client_telephone = client_telephone, client_adress = client_adress,
                client_neighborhood = client_neighborhood,client_zip = client_zip,client_city = client_city,client_state = client_state)
            
            client_data.save()

            purchase_data = PurchaseData(store_name = store_name, receipt_number = receipt_number, purchase_date = purchase_date,
                product_code = product_code,price = price)
            
            purchase_data.save()

            equipment_data = EquipmentData(equipment_name = equipment_name, brand = brand, new = new, model = model, serial_number = serial_number,
                user_password = user_password, defect = defect, state = state, acessories = acessories,observations = observations, files = files)

            equipment_data.save()



            return HttpResponse('Thanks, ' + client_data.client_name)
        else:
            form = CreateServiceOrder()

        return redirect('pagina-os-ativas')