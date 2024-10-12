from django.shortcuts import render
from .models import Arquivo, Cartao
from django.http import FileResponse
from django.utils.decorators import decorator_from_middleware
from django.middleware.cache import CacheMiddleware
from django.core.paginator import Paginator
from .forms import BuscaForm
from datetime import date, timedelta
from django.db.models import Q
import re


# Create your views here.
def home(request):
    cartoes = Cartao.objects.all()
    return render(request, 'home.html', {'cartoes': cartoes})

def cadastro(request):
  return render(request, 'cadastro.html')

def dicas(request):
  return render(request, 'dicas.html')

def entrar(request):
  return render(request, 'entrar.html')

def fale_conosco(request):
  return render(request, 'fale_conosco.html')

def imprensa(request):
  documentos = Arquivo.objects.all()
  return render(request, 'imprensa.html', {'List': documentos})

#def testes(request):
 # documentos = Arquivo.objects.all()
  #return render(request, 'testes.html', {'List': documentos})

def livros(request):
  return render(request, 'livros.html')

def sobre(request):
  return render(request, 'sobre.html')

def buscar_arquivos(request):
    form = BuscaForm(request.GET)
    arquivos = Arquivo.objects.all()

    if form.is_valid():
        # Ordenação
        ordenacao = form.cleaned_data.get('ordenacao')
        if ordenacao == 'mais_recentes':
            arquivos = arquivos.order_by('-data')
        elif ordenacao == 'mais_antigos':
            arquivos = arquivos.order_by('data')

        # Período
        periodo = form.cleaned_data.get('periodo')
        if periodo == 'ultimo_mes':
            um_mes_atras = date.today() - timedelta(days=30)
            arquivos = arquivos.filter(data__gte=um_mes_atras)
        elif periodo == 'ultimos_3_meses':
            tres_meses_atras = date.today() - timedelta(days=90)
            arquivos = arquivos.filter(data__gte=tres_meses_atras)
        elif periodo == 'ultimos_6_meses':
            seis_meses_atras = date.today() - timedelta(days=180)
            arquivos = arquivos.filter(data__gte=seis_meses_atras)

        # Fonte
        fonte = form.cleaned_data.get('fonte')
        if fonte and fonte != 'todas':
            arquivos = arquivos.filter(fonte=fonte)

        # Assunto
        assunto = form.cleaned_data.get('assunto')
        if assunto:
            arquivos = arquivos.filter(assunto__icontains=assunto)

        # Barra de Pesquisa
        barra_pesquisa = request.GET.get('barra_pesquisa', '')
        if barra_pesquisa:
            termos = barra_pesquisa.split()
            arquivos_filtrados = arquivos
            for termo in termos:
                arquivos_filtrados = arquivos_filtrados.filter(
                    Q(temas__icontains=termo) | 
                    Q(assunto__icontains=termo) | 
                    Q(filme__icontains=termo)
                )
            arquivos = arquivos_filtrados

    # Paginação
    paginator = Paginator(arquivos, 25)  # 25 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'imprensa_resultados.html', {'form': form, 'page_obj': page_obj, 'arquivos': page_obj.object_list})
