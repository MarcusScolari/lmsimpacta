# Generated by Django 2.1.3 on 2018-12-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restrito', '0002_auto_20181204_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='conteudo',
            field=models.TextField(max_length=255),
        ),
    ]