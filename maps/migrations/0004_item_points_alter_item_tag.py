# Generated by Django 4.1.4 on 2023-04-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_remove_item_map_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.TextField(blank=True, null=True),
        ),
    ]
