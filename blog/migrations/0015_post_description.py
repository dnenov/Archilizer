# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='default description', max_length=60),
            preserve_default=False,
        ),
    ]
