# Generated by Django 4.0.3 on 2022-05-08 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0003_alter_weapon_damages_alter_weapon_penalty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weapon',
            options={'ordering': ['type', 'name']},
        ),
    ]
