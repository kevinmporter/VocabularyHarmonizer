# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='description',
            field=models.CharField(default='Default description', max_length=2048),
            preserve_default=False,
        ),
    ]