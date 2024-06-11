from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import ChangeOrderStatusForm, CreateServiceOrder
from .models import CustomerData, ClientData, PurchaseData, BuyerData, EquipmentData, EmployeeData, ServiceOrder
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
import uuid
from datetime import datetime

class ChangeOrderStatus2(View):
    def get(self, request):
        return render(request, 'app_chatbot/ChangeOrderStatus.html')


class HomePage(View):
    def get(self, request):
        return render(request, 'app_chatbot/HomePage.html')
    

class Modal(View):
    def get(self,request):
        return render(request, 'app_chatbot/TemporaryPages/GuideModal/modal.html')


class CustomerPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/CustomerPage.html')


class CustomerOrders(View):
    def get(self, request):
        # return render(request, 'app_chatbot/CustomerOrdersPage.html')
        return render(request, 'app_chatbot/CustomerOrdersPage.html')


class OrdemServicoView(View):
    def get(self, request):
        return render(request, 'app_chatbot/os.html')
    
    def post(self, request):
        if request.method == "POST":
            form = request.POST
            dados_cliente = ClientData(
                nome_cliente=form["nome_cliente"], cpf_cnpj =form["id_cliente"], rg_ie=form["sub_id_cliente"], data_nascimento_cliente=form["data_nascimento_cliente"],
                email_cliente=form["email_cliente"], celular_cliente=form["celular_cliente"], telefone_cliente=form["telefone_cliente"], endereco_cliente=form["endereco_cliente"],
                bairro_cliente=form["bairro_cliente"], cep_cliente=form["cep_cliente"], cidade_cliente=form["cidade_cliente"], uf_cliente=form["uf_cliente"]
                )
            dados_cliente.save()

            dados_comprador = BuyerData(
                nome_comprador=form["nome_comprador"], cpf_cnpj =form["id_comprador"], rg_ie=form["sub_id_comprador"], data_nascimento_comprador=form["data_nascimento_comprador"],
                email_comprador=form["email_comprador"], celular_comprador=form["celular_comprador"], telefone_comprador=form["telefone_comprador"], endereco_comprador=form["endereco_comprador"],
                bairro_comprador=form["bairro_comprador"], cep_comprador=form["cep_comprador"], cidade_comprador=form["cidade_comprador"], uf_comprador=form["uf_comprador"]
                )
            dados_comprador.save()

            dados_compra = PurchaseData(
                nome_loja =form["loja"], num_nf=form["nf"], data_compra=form["data_compra"],
                cod_produto=form["cod_produto"], valor=form["valor"]
                )
            dados_compra.save()

            dados_equipamento = EquipmentData(
                nome_equipamento=form["equipamento"], marca =form["marca"], lacrado=form["estado_lacre"], modelo=form["modelo"],
                num_serie=form["num_serie"], senha_usuario=form["senha_usuario"], defeito=form["texto_defeito"], estado=form["estado_aparelho"],
                acessorios=form["acessorios"], observacoes=form["observacoes"], arquivos=form["arquivos"]
                )
            dados_equipamento.save()


        return render(request, 'app_chatbot/os.html')


class OrdemServicoAtivaView(View):
    def get(self, request):
        return render(request, 'app_chatbot/os_ativas.html')
    
    def post(self, request):
        service_order = ServiceOrder.objects.all()
        protocol_code = request.POST['protocol_code']

        for order in service_order:
            if protocol_code == order.protocol_code:
                return render(request, 'app_chatbot/os_ativas.html', {'protocol_code': order})
            
        return HttpResponse("Hello!")
         

# TODO: transformar CancelOrder em função, para ser chamada tanto pelo cliente quanto pelo funcionário
class CancelOrder(View):
    def get(self, request, order_id):
        ordem_servico = get_object_or_404(ServiceOrder, id=order_id)
        return render(request, 'app_chatbot/TemporaryPages/CancelOrder/cancel_order.html', {'ordem_servico': ordem_servico})

    def post(self, request, order_id):
        ordem_servico = get_object_or_404(ServiceOrder, id=order_id)
        if ordem_servico.status != 'Cancelada':
            ordem_servico.status = 'Cancelada'
            ordem_servico.save()
        return redirect('order_detail', order_id=order_id) # TODO: redirect


class ChangeOrderStatus(View):
    def get(self, request, order_id):
        ordem_servico = get_object_or_404(ServiceOrder, id=order_id)
        form = ChangeOrderStatusForm(instance=ordem_servico)
        return render(request, 'app_chatbot/TemporaryPages/ChangeOrderStatus/change_order_status.html', {'form': form, 'ordem_servico': ordem_servico})

    def post(self, request, order_id):
        ordem_servico = get_object_or_404(ServiceOrder, id=order_id)
        form = ChangeOrderStatusForm(request.POST, instance=ordem_servico)
        if form.is_valid():
            ordem_servico = form.save(commit = False)
            if ordem_servico.status == 'Concluída':
                ordem_servico.is_finished = True
            form.save()
            ordem_servico.sms()
            return redirect('success_page')  # TODO: redirect
        return render(request, 'app_chatbot/TemporaryPages/ChangeOrderStatus/change_order_status.html', {'form': form, 'ordem_servico': ordem_servico})
 

class ServiceOrderListView(View):
    def get(self, request):
        service_order = ServiceOrder.objects.all()
        service_order_date = ServiceOrder.objects.values('create_date').distinct()
        service_order_status = ServiceOrder.objects.values('status').distinct()
        filtro = False
        return render(request, 'app_chatbot/teste_os_ativas.html', {'service_order': service_order, 'service_order_date': service_order_date,
                                                                    'service_order_status': service_order_status,'filtro': filtro})
    
    def post(self, request):
        service_order = ServiceOrder.objects.all()
        service_order_date = ServiceOrder.objects.values('create_date').distinct()
        service_order_status = ServiceOrder.objects.values('status').distinct()
        filtro = True
        choosen_status = request.POST['choosen_status']
        choosen_date_post= request.POST['choosen_date']

        if choosen_date_post == 'Todos':
            choosen_date = choosen_date_post
        else:
            choosen_date = datetime.strptime(choosen_date_post, '%d/%m/%Y').date()        
            
        return render(request, 'app_chatbot/teste_os_ativas.html', {'service_order': service_order, 'service_order_date': service_order_date,
                                                                    'service_order_status': service_order_status,'choosen_status': choosen_status, 
                                                                    'choosen_date': choosen_date, 'filtro': filtro})


class ServiceOrderView(View):
    def get(self, request):
        form = CreateServiceOrder()
        ctx = {'form': form}
        return render(request, 'app_chatbot/service_order.html', ctx)
    
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

            protocol_code = (str(uuid.uuid4())[:8]).upper()
            service_order_data = ServiceOrder(client_data = client_data, buyer_data = buyer_data, purchase_data = purchase_data,
                                              equipment_data = equipment_data, protocol_code = protocol_code)
            
            service_order_data.save()

            return HttpResponse('Thanks, ' + client_data.client_name + '. Write down your protocol code: ' + service_order_data.protocol_code)
        else:
            form = CreateServiceOrder()

        return redirect('pagina-os-ativas')