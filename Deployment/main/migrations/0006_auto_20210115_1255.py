# Generated by Django 3.1.4 on 2021-01-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210112_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setmodels',
            name='setDateLock',
        ),
        migrations.AddField(
            model_name='setmodels',
            name='setDatumeLock',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='setmodels',
            name='setID',
            field=models.CharField(default='CURUBPIT7T5VDY61K4DF', max_length=20),
        ),
    ]
