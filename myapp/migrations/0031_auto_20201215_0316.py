# Generated by Django 3.1.2 on 2020-12-15 08:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20201215_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 15, 8, 16, 45, 847234, tzinfo=utc)),
        ),
    ]