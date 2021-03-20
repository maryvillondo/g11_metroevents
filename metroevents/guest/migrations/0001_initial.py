# Generated by Django 3.1.4 on 2021-03-20 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('user_pword', models.CharField(blank=True, max_length=50, null=True)),
                ('register_date', models.DateField(default=datetime.datetime(2021, 3, 20, 15, 31, 27, 924560))),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
