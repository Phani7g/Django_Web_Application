# Generated by Django 3.1.2 on 2020-12-14 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20201214_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 14, 18, 18, 22, 113520, tzinfo=utc)),
        ),
    ]