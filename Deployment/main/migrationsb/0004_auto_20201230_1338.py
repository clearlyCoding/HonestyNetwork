# Generated by Django 3.1.4 on 2020-12-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_setmodels_setrepitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='setmodels',
            name='setReady',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='setmodels',
            name='setUsers',
            field=models.JSONField(blank=True, default='', max_length=500000),
        ),
    ]