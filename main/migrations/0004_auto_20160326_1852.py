# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160326_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('badge', models.ImageField(upload_to=b'', verbose_name='Badge')),
                ('url', models.URLField(verbose_name='Link')),
            ],
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-rating']},
        ),
    ]
