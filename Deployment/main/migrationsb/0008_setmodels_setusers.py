# Generated by Django 3.1.4 on 2020-12-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_setmodels_setusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='setmodels',
            name='setUsers',
            field=models.JSONField(blank=True, default='', max_length=500000),
        ),
    ]
