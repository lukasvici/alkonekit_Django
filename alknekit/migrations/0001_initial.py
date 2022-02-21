# Generated by Django 4.0.2 on 2022-02-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(default=None, max_length=16, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(default=1, max_length=20)),
                ('tittle', models.CharField(max_length=50)),
                ('articul', models.CharField(max_length=75, unique=True)),
                ('images', models.ImageField(upload_to='')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
