# Generated by Django 4.1.3 on 2023-02-25 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2023, 2, 25, 2, 8, 35, 539265, tzinfo=datetime.timezone.utc))),
                ('creator', models.CharField(max_length=50)),
            ],
        ),
    ]
