# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20160622_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]