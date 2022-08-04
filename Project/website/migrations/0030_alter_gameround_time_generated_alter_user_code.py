# Generated by Django 4.0 on 2022-07-31 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_alter_gameround_week_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameround',
            name='time_generated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='a4oFdJ8j', max_length=8, null=True, unique=True),
        ),
    ]
