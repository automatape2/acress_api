# Generated by Django 3.2.25 on 2024-08-05 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubinei', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poblacion',
            name='value',
            field=models.CharField(default='-', max_length=100),
        ),
    ]