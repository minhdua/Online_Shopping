# Generated by Django 3.0 on 2019-12-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20191228_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='token',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
