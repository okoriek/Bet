# Generated by Django 4.0 on 2022-07-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_userhistory_options_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='7sN99hmp', max_length=8, null=True, unique=True),
        ),
    ]