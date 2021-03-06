# Generated by Django 3.1.4 on 2021-03-22 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0005_auto_20210322_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=50, null=True)),
                ('event_date', models.DateField()),
                ('num_participants', models.IntegerField()),
                ('num_interested', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Events_Users', to='guest.users')),
            ],
            options={
                'db_table': 'Events',
            },
        ),
    ]
