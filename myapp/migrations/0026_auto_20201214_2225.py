# Generated by Django 3.1.2 on 2020-12-15 03:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20201214_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 15, 3, 25, 1, 785251, tzinfo=utc)),
        ),
    ]