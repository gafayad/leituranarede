from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError
import re
from datetime import datetime
# Create your models here.

class Cartao(models.Model):
    nome = models.CharField(max_length=100)
    imagem_url = models.URLField(blank=True, null=True)
    imagem_upload = models.ImageField(upload_to='cartoes/', blank=True, null=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=900)
    ordem = models.PositiveIntegerField()

    class Meta:
        ordering = ['ordem']
        db_table = 'Cartões'

    def __str__(self):
        return self.titulo

    def clean(self):
        if not self.imagem_url and not self.imagem_upload:
            raise ValidationError('Você deve fornecer um link ou fazer o upload de uma imagem.')
        if self.imagem_url and self.imagem_upload:
            raise ValidationError('Você deve preencher apenas um dos campos: link ou upload de imagem.')

    def get_imagem(self):
        if self.imagem_url:
            return self.imagem_url
        elif self.imagem_upload:
            return self.imagem_upload.url
        return None

class Usuario(models.Model):
  usuario = models.ForeignKey(User,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.usuario

class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='pdf/', blank=False, max_length=500)
    temas = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(null=True, blank=True)
    assunto = models.CharField(max_length=255, blank=True, null=True)
    filme = models.TextField(blank=True, null=True)
    fonte = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Arquivos'

    def __unicode__(self):
        return self.arquivo.name

    def save(self, *args, **kwargs):
        if self.arquivo:
            self.arquivo.name = self.arquivo.name.replace('uploads/', '')
            info = self.process_filename(self.arquivo.name)
            self.temas = ', '.join(info['temas']) if info['temas'] else ''
            self.data = datetime.strptime(info['data'], '%d/%m/%Y').date() if info['data'] else None
            self.assunto = info['assunto'] if info['assunto'] else ''
            self.filme = info['filme'] if info['filme'] else ''
            self.fonte = info['fonte'] if info['fonte'] else ''
        super().save(*args, **kwargs)

    @staticmethod
    def process_filename(filename):
        # Remover o pdf/:
        nomeBase = filename.split('/')[-1]

        # Data como separador entre os temas e o resto:
        partes = re.split(r' \d{6} - ', nomeBase)

        # Parte 1 - temas:
        parte1 = partes[0]
        temas = parte1.split(' e ')

        # Data e formatação dela:
        procData = re.search(r'\d{6}', nomeBase)
        dataNum = procData.group()
        data = datetime.strptime(dataNum, '%y%m%d').strftime('%d/%m/%Y')

        # Parte 2 - Assunto, filme e fonte:
        if ';' in partes[1]:
            parte2 = re.split(r';', partes[1])
            # Assunto:
            assunto = parte2[0]

            # Resumo e Fonte:
            filme = ''
            if len(parte2) > 1:
                # Começar com a segunda parte (parte2[1]) e adicionar o resto
                filme = parte2[1]
                for extra_part in parte2[2:]:
                    filme += " -" + extra_part
        else:
            # Sem ';', o assunto é vazio e o filme é o restante do texto após a data
            assunto = ""
            filme = partes[1]

        # Remover .pdf e fonte do filme:
        filme = re.sub(r'(?:\s*|[_\s])?(estadão|fsp|editorial)\s*(\([0-9]+\))?\s*\.pdf$', '', filme, flags=re.I).strip()

        # Remover .pdf sozinho:
        if filme.endswith('.pdf'):
            filme = filme[:-4]

        # Caso de Foto:
        foto_match = re.search(r'\b(FOTO|FOTOs)\b', filme, flags=re.I)
        # Se o texto tiver Foto:
        if foto_match:
            foto = f"{foto_match.group().upper()}"
            partes_resumo = re.split(r'\b(FOTO|FOTOs)\b', filme, maxsplit=1, flags=re.I)
            texto_principal = partes_resumo[0].strip().rstrip('_,. ')
            descricao_foto = partes_resumo[2].strip() if len(partes_resumo) > 2 else ""

            # Se a foto tiver descrição:
            if descricao_foto:
                filme = f"{texto_principal}. {foto}: {descricao_foto}"
            else:
                filme = f"{texto_principal}. {foto}"
        # Se não:
        else:
            filme = filme.rstrip('-,; ')

        # Ponto final no filme:
        filme = filme + "."

        # Definir as fontes:
        fonte = "O Globo"  # Valor padrão
        if 'fsp' in partes[1].lower() or 'editorial fsp' in partes[1].lower():
            fonte = "Folha de S. Paulo"
        elif 'estadão' in partes[1].lower() or 'editorial estadão' in partes[1].lower():
            fonte = "Estadão"

        return {
            'partes': partes,
            'temas': temas,
            'data': data,
            'assunto': assunto,
            'filme': filme,
            'fonte': fonte
        }
