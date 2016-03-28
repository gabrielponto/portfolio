# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'title', verbose_name='Slug', editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='background',
            field=models.ImageField(upload_to=b'img/block', verbose_name='Plano de Fundo', blank=True),
        ),
        migrations.AlterField(
            model_name='blockcase',
            name='logo',
            field=models.ImageField(upload_to=b'img/blockcase', verbose_name=b'Logo'),
        ),
    ]
