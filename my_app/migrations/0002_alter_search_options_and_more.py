# Generated by Django 4.0.2 on 2022-02-24 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.RenameField(
            model_name='search',
            old_name='created_at',
            new_name='created',
        ),
    ]
