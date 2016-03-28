# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('text', models.TextField(verbose_name='Texto')),
                ('position', models.IntegerField(verbose_name='Posi\xe7\xe3o')),
                ('background', models.ImageField(upload_to=b'', verbose_name='Plano de Fundo')),
                ('background_color', models.CharField(max_length=7, verbose_name=b'Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('content', models.TextField(verbose_name='Conte\xfado')),
            ],
        ),
        migrations.CreateModel(
            name='BlockCase',
            fields=[
                ('block_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Block')),
                ('logo', models.ImageField(upload_to=b'', verbose_name=b'Logo')),
                ('case', models.ForeignKey(to='main.Case')),
            ],
            bases=('main.block',),
        ),
    ]
