# Generated by Django 4.1 on 2022-12-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0028_remove_charactersheet_skill_set'),
        ('chroniques', '0009_newschronicle_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newschronicle',
            name='new_members',
            field=models.ManyToManyField(blank=True, related_name='new_members', to='fiches.charactersheet'),
        ),
    ]
