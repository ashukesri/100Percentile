# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20180604_1603'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionImages',
            new_name='QuestionImage',
        ),
    ]
