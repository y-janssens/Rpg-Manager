# Generated by Django 4.1 on 2022-09-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapshot',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
