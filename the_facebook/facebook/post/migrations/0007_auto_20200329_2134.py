# Generated by Django 2.2.1 on 2020-03-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200328_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
