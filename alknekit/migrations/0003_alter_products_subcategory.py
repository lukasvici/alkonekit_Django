# Generated by Django 4.0.2 on 2022-02-21 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alknekit', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='subcategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alknekit.category'),
        ),
    ]