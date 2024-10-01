from django.contrib import admin
from .models import Usuario
from .models import Arquivo 
from .models import Cartao

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('nome','titulo', 'ordem')
    ordering = ('ordem',)

# Register your models here.
class ReferenciaUsuario(admin.ModelAdmin):
  list_display=['usuario']

admin.site.register(Usuario, ReferenciaUsuario)

class ReferenciaArquivo(admin.ModelAdmin):
  list_display=['arquivo']

admin.site.register(Arquivo, ReferenciaArquivo)