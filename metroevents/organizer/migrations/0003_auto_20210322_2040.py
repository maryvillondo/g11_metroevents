# Generated by Django 3.1.4 on 2021-03-22 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20210322_2036'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='events',
            table='me_events',
        ),
    ]
