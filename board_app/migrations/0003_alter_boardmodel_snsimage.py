# Generated by Django 3.2.3 on 2021-08-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0002_rename_readtext_boardmodel_read_user_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='snsimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
