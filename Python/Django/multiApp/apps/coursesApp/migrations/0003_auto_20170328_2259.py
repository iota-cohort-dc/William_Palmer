# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0002_loginr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoginR',
            new_name='UsersCourses',
        ),
    ]
