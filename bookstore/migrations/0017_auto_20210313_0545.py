# Generated by Django 2.0.3 on 2021-03-13 05:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0016_auto_20210308_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 5, 45, 14, 983998, tzinfo=utc)),
        ),
    ]
