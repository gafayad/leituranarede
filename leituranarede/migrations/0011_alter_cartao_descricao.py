# Generated by Django 5.0.2 on 2024-10-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leituranarede', '0010_alter_cartao_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='descricao',
            field=models.TextField(max_length=850),
        ),
    ]
