from .models import presente, Convidado
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def tela_inicial(request):
    return render(request, 'casamento/tela_inicial.html')

def local_casamento(request):
    return render(request, 'casamento/local_casamento.html')
def listapresentes(request):
    items = presente.objects.all().order_by('nome')
    paginator = Paginator(items, 5)
    page = request.GET.get('page')
    try:
        presentes = paginator.page(page)
    except PageNotAnInteger:
        presentes = paginator.page(1)
    except EmptyPage:
        presentes = paginator.page(paginator.num_pages)

    return render(request, 'casamento/lista_presentes.html', {'presentes':presentes})

def presenca(request):
    return render(request, 'casamento/presenca.html')
def linkpresente(request):
    return render(request, 'casamento/link_presentes.html')
def contato(request):
    return render(request, 'casamento/contato.html')
def postconfirmacao(request):
    if request.method == "POST":
        nome = request.POST.get('nome', False)
        presenca = request.POST.get('presenca', False)
        pessoas = request.POST.get('pessoas', False)

        if presenca == 'sim':
            presenca = True
        else:
            presenca = False

        convidado = Convidado.objects.create(nome=nome, presenca=presenca, npessoas=pessoas)
        convidado.publish()

        return HttpResponseRedirect('/agradecimento')

def agradecimento(request):
    return render(request, 'casamento/agradecimento.html')
