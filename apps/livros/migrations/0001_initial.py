# Generated by Django 4.1 on 2022-08-30 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('nacionalidade', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=150)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=50)),
                ('qtd_paginas', models.IntegerField(verbose_name='Quantidade de páginas')),
                ('ano_pub', models.IntegerField(verbose_name='Ano de publicação')),
                ('resenha', models.TextField()),
                ('capa', models.ImageField(upload_to='capas/')),
                ('onde_comprar', models.URLField(verbose_name='Onde comprar')),
                ('livro_pdf', models.FileField(upload_to='livros/', verbose_name='Livro em PDF')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicar livro')),
                ('autor', models.ManyToManyField(to='livros.autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.editora')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]