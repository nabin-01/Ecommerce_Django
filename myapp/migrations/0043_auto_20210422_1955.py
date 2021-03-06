# Generated by Django 3.1.7 on 2021-04-22 14:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_auto_20210422_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=200)),
                ('slug', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('checkout', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], default='active', max_length=100)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=200)),
                ('net_total', models.IntegerField(default=0)),
                ('slug', models.CharField(default=None, max_length=100, unique=True)),
                ('shipping_cost', models.IntegerField(default=0)),
                ('grand_total', models.IntegerField(default=0)),
                ('checkout', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=200)),
                ('first_name', models.CharField(default=None, max_length=200)),
                ('last_name', models.CharField(default=None, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('shipping_add', models.CharField(max_length=200)),
                ('mobile_no', models.IntegerField()),
                ('checkout', models.BooleanField(default=True)),
                ('date_checked', models.DateTimeField(default=django.utils.timezone.now)),
                ('products', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='carts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='Carts',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
