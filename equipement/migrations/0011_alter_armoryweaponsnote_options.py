# Generated by Django 4.0.3 on 2022-08-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0010_alter_armoryweaponsnote_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armoryweaponsnote',
            options={'ordering': ['-type', 'name', 'title']},
        ),
    ]
