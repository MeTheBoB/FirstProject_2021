# Generated by Django 2.2.1 on 2020-03-30 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20200329_2312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
