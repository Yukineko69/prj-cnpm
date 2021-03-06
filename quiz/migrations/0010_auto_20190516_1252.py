# Generated by Django 2.0.7 on 2019-05-16 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190516_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionattempt',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Submitted date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date published'),
        ),
    ]
