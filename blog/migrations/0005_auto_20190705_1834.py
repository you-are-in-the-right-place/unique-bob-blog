# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-07-05 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_announce_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/%Y/%m/%d/'),
        ),
    ]
