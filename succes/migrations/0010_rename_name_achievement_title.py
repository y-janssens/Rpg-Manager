# Generated by Django 4.0.3 on 2022-08-13 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('succes', '0009_achievement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='name',
            new_name='title',
        ),
    ]
