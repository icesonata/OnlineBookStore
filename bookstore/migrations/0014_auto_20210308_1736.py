# Generated by Django 2.0.3 on 2021-03-08 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0013_auto_20210308_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 17, 36, 38)),
        ),
    ]