# Generated by Django 3.2.25 on 2024-08-07 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoPeru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('idccpp', models.CharField(max_length=50)),
            ],
        ),
    ]
