# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20180526_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswers',
            name='answerType',
            field=models.PositiveIntegerField(choices=[(1, 'subjective'), (2, 'objetive')], default=1),
        ),
        migrations.AlterField(
            model_name='questionanswers',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='questionimages',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='questions',
            name='difficultyLevel',
            field=models.CharField(choices=[(1, 'Basic'), (2, 'Mediam'), (3, 'Hard')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='thrasoldTime',
            field=models.TimeField(default='2 minute'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='type',
            field=models.CharField(choices=[(1, 'subjective'), (2, 'objetive')], max_length=100),
        ),
    ]
