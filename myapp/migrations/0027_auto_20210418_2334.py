# Generated by Django 3.1.7 on 2021-04-18 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_remove_carttotal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttotal',
            name='slug',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='carttotal',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.cart'),
        ),
    ]
