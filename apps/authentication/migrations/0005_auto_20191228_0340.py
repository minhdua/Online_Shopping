# Generated by Django 3.0 on 2019-12-28 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20191228_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
