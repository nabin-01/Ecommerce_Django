# Generated by Django 3.1.7 on 2021-04-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_carttotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carttotal',
            name='cart',
        ),
        migrations.AddField(
            model_name='carttotal',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
    ]
