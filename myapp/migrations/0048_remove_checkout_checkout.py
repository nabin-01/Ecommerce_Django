# Generated by Django 3.1.7 on 2021-04-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_auto_20210422_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='checkout',
        ),
    ]
