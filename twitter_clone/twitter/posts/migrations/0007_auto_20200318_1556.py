# Generated by Django 2.2.1 on 2020-03-18 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_date_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.TimeField(default=datetime.datetime(2020, 3, 18, 15, 56, 20, 255270)),
        ),
    ]
