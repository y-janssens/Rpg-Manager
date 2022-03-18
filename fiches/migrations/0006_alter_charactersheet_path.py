# Generated by Django 4.0.3 on 2022-03-18 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrieres', '0005_remove_carriere_att1v_remove_carriere_att2v_and_more'),
        ('fiches', '0005_alter_charactersheet_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersheet',
            name='path',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrieres.carriere'),
        ),
    ]
