# Generated by Django 2.1.2 on 2018-10-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('famleague', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='city',
        ),
    ]
