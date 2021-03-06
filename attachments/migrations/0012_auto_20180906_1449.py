# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0011_session_allowed_file_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='allowed_file_extensions',
            field=models.TextField(blank=True, help_text='Whitespace-separated file extensions that are allowed for upload.'),
        ),
        migrations.AlterField(
            model_name='session',
            name='allowed_file_types',
            field=models.TextField(blank=True, help_text='White list of file types that are allowed for upload, separated by new line. Used as a fallback if file mimetype is not known.'),
        ),
    ]
