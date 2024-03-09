# Generated by Django 4.1.4 on 2024-03-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download', models.FileField(blank=True, null=True, upload_to='versions')),
            ],
        ),
        migrations.RemoveField(
            model_name='version',
            name='url',
        ),
    ]
