# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_term_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='description',
            field=models.CharField(default='Default', max_length=2048),
            preserve_default=False,
        ),
    ]
