# Generated by Django 2.2.1 on 2020-03-18 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200318_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_posted_date',
            field=models.TimeField(default=datetime.date(2020, 3, 18)),
        ),
    ]
