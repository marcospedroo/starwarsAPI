# Generated by Django 3.1.2 on 2020-11-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetas', '0003_auto_20201103_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeta',
            name='terreno',
            field=models.CharField(choices=[('DE', 'Deserto'), ('OC', 'Oceano'), ('FL', 'Florestas'), ('MO', 'Montanhoso'), ('TU', 'Tundra'), ('PA', 'Pantano')], max_length=200),
        ),
    ]
