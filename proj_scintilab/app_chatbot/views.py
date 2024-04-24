from django.shortcuts import render
from django.views import View
from .forms import OrdemServico

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'app_chatbot/base.html')
    
class OrdemServicoView(View):
    def get(self, request):
        form = OrdemServico
        return render(request, 'app_chatbot/os.html', {'form': OrdemServico})