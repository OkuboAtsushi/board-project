# Generated by Django 3.2.3 on 2021-08-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0003_alter_boardmodel_snsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='snsimage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
