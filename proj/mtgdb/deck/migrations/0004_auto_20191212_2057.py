# Generated by Django 3.0 on 2019-12-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0003_auto_20191212_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='name',
            new_name='deck_name',
        ),
    ]
