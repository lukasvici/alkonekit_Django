# Generated by Django 3.2.12 on 2022-02-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alknekit', '0013_alter_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Subcategory',
            field=models.CharField(max_length=50),
        ),
    ]
