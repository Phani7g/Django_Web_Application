# Generated by Django 3.1.2 on 2020-11-24 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20201123_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 24, 2, 30, 45, 262404, tzinfo=utc)),
        ),
    ]
