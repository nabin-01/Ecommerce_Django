# Generated by Django 3.1.7 on 2021-04-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_carttotal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttotal',
            name='shipping_cost',
            field=models.IntegerField(default=0),
        ),
    ]
