# Generated by Django 3.1.2 on 2020-11-24 05:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20201123_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 24, 5, 21, 17, 848549, tzinfo=utc)),
        ),
    ]
