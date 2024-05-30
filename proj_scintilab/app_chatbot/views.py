from django.shortcuts import render
from django.views import View
from .models import DadosCliente, DadosCompra, DadosComprador, DadosEquipamento
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator


class HomePage(View):
    def get(self, request):
        return render(request, 'app_chatbot/HomePage.html')
    
class ChatbotView(View):
    def get(self, request):
        return render(request, 'app_chatbot/chatbot.html')
    
class OrdemServicoView(View):
    def get(self, request):
        return render(request, 'app_chatbot/os.html')

class CustomerLoginPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/CustomerLoginPage.html')
    
class EmployeeLoginPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/EmployeeLoginPage.html')
    
class CustomerRegisterPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/CustomerRegisterPage.html')
    
class EmployeeRegisterPage(View):
    def get(self, request):
        return render(request, 'app_chatbot/EmployeeRegisterPage.html')


    
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
