# Generated by Django 3.2.10 on 2022-03-01 22:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceAreaModel',
            new_name='ServiceArea',
        ),
    ]