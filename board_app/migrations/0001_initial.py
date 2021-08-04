# Generated by Django 3.2.5 on 2021-07-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('snsimage', models.ImageField(upload_to='')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readtext', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
