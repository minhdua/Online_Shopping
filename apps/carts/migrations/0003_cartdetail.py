# Generated by Django 3.0 on 2020-01-08 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bills', '0001_initial'),
        ('products', '0001_initial'),
        ('carts', '0002_delete_cartdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.IntegerField(default=1)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('bill', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bills.Bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
