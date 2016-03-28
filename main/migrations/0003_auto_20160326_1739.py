# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160314_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('rating', models.IntegerField(verbose_name='Nota')),
                ('color', models.CharField(max_length=7, verbose_name='Cor')),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='Conte\xfado'),
        ),
    ]
