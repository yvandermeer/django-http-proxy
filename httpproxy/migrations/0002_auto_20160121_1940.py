# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('httpproxy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestparameter',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='response',
            name='content_type',
            field=models.CharField(max_length=200, verbose_name='content type'),
        ),
    ]
