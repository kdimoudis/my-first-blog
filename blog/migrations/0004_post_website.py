# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170102_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.URLField(null=True, verbose_name='Website'),
        ),
    ]
