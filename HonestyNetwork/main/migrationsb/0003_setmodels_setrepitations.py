# Generated by Django 3.1.4 on 2020-12-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201230_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='setmodels',
            name='setRepitations',
            field=models.CharField(choices=[('WKLY', 'Weekly'), ('MTHY', 'Monthly')], default='MTHY', max_length=4),
        ),
    ]