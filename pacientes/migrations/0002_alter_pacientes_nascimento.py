# Generated by Django 5.1.4 on 2025-01-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
