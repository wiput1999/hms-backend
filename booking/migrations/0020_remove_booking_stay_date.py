# Generated by Django 2.2 on 2019-05-03 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_auto_20190503_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='stay_date',
        ),
    ]
