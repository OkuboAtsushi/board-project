# Generated by Django 3.2.3 on 2021-08-01 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='readtext',
            new_name='read_user_ids',
        ),
    ]