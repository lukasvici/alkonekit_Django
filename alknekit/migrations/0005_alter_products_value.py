# Generated by Django 3.2.12 on 2022-02-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alknekit', '0004_products_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Value',
            field=models.FloatField(default=None),
        ),
    ]
