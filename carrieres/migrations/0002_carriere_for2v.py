# Generated by Django 4.0.3 on 2022-03-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrieres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carriere',
            name='For2V',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
