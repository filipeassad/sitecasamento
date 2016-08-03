from .models import presente
from django.shortcuts import render

# Create your views here.

def tela_inicial(request):
    return render(request, 'casamento/tela_inicial.html')

def local_casamento(request):
    return render(request, 'casamento/local_casamento.html')
def listapresentes(request):
    items = presente.objects.all().order_by('nome')
    return render(request, 'casamento/lista_presentes.html', {'presentes':items})
def presenca(request):
    return render(request, 'casamento/presenca.html')
