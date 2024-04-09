from django.shortcuts import render
from django.views import View

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'app_chatbot/base.html')
