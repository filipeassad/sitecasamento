from django.shortcuts import render

# Create your views here.

def tela_inicial(request):
    return render(request, 'casamento/tela_inicial.html')
