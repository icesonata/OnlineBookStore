# Generated by Django 2.0.3 on 2021-03-08 18:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_auto_20210308_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 18, 11, 5, 15460, tzinfo=utc)),
        ),
    ]
