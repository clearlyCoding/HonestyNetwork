# Generated by Django 3.1.4 on 2020-12-30 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201230_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setmodels',
            name='setUsers',
        ),
    ]
