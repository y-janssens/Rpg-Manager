# Generated by Django 4.1.4 on 2023-01-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineage', '0002_alter_character_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='heirs',
            field=models.ManyToManyField(blank=True, related_name='_heirs', to='lineage.character'),
        ),
    ]
