# Generated by Django 3.1.1 on 2021-03-22 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_auto_20210322_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 22, 23, 9, 39, 653561)),
        ),
    ]