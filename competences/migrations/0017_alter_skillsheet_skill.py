# Generated by Django 4.0.3 on 2022-05-01 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0016_alter_skillsheet_owner_alter_skillsheet_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsheet',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competences.skill'),
        ),
    ]