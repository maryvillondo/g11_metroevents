# Generated by Django 3.1.4 on 2021-03-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_requests_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='req_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
