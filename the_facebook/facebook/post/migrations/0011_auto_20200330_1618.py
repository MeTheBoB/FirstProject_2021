# Generated by Django 2.2.1 on 2020-03-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20200330_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
