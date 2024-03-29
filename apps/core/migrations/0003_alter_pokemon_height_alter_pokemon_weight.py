# Generated by Django 4.1.7 on 2023-03-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_weight_pokemon_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.PositiveIntegerField(help_text='Height of the pokemon in centimeters', verbose_name='Pokemon height'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.PositiveIntegerField(help_text='Pokemon weight in grams', verbose_name='Pokemon weight'),
        ),
    ]
