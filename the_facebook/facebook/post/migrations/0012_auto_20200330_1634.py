# Generated by Django 2.2.1 on 2020-03-30 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200330_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
