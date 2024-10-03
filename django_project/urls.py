"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from leituranarede import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.home),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dicas/', views.dicas, name='dicas'),
    path('entrar/', views.entrar, name='entrar'),
    path('contato/', views.fale_conosco, name='fale_conosco'),
    path('imprensa/', views.imprensa, name='imprensa'),
    #path('testes/', views.testes, name='testes'),
    path('livros/', views.livros, name='livros'),
    path('sobre/', views.sobre, name='sobre'),
    path('buscar/', views.buscar_arquivos, name='buscar_arquivos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)