# Generated by Django 3.1.2 on 2020-12-12 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20201212_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 12, 16, 47, 11, 557150, tzinfo=utc)),
        ),
    ]
