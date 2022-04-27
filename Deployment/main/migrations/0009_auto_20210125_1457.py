# Generated by Django 3.1.4 on 2021-01-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210115_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setmodels',
            name='setDelinquents',
        ),
        migrations.AddField(
            model_name='setmodels',
            name='setPaid',
            field=models.JSONField(blank=True, default=dict, max_length=500000),
        ),
        migrations.AlterField(
            model_name='setmodels',
            name='setID',
            field=models.CharField(default='8ZXKWJEV3UIU8NBYJHS5', max_length=20),
        ),
    ]