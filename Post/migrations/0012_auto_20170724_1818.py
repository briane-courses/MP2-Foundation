# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0011_auto_20170722_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_coursefk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.Course'),
        ),
    ]