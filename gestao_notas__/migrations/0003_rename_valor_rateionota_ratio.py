# Generated by Django 5.0.2 on 2024-04-11 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_notas', '0002_rateionota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rateionota',
            old_name='valor',
            new_name='ratio',
        ),
    ]
