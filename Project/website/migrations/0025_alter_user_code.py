# Generated by Django 4.0 on 2022-07-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='0hxXOlmZ', max_length=8, null=True, unique=True),
        ),
    ]
