from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class BuscaForm(forms.Form):
  ordenacao_choices = [
      ('mais_recentes', 'Mais recentes'),
      ('mais_antigos', 'Mais antigos'),
  ]

  periodo_choices = [
      ('completo', 'Completo'),
      ('ultimo_mes', 'Último mês'),
      ('ultimos_3_meses', 'Últimos 3 meses'),
      ('ultimos_6_meses', 'Últimos 6 meses'),
      ('de_ate', 'De / até:'),
  ]

  fontes_choices = [
      ('Estadão', 'Estadão'),
      ('O Globo', 'O Globo'),
      ('Folha de S. Paulo', 'Folha de S. Paulo'),
  ]

  ordenacao = forms.ChoiceField(choices=ordenacao_choices, required=False)
  periodo = forms.ChoiceField(choices=periodo_choices, required=False)
  fonte = forms.ChoiceField(choices=fontes_choices, required=True)
  dataInicio = forms.DateField(required=False)
  dataFim = forms.DateField(required=False)
  assunto = forms.CharField(max_length=255, required=False)