# Generated by Django 3.1.2 on 2020-12-12 16:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20201201_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 12, 16, 33, 24, 451887, tzinfo=utc)),
        ),
    ]
