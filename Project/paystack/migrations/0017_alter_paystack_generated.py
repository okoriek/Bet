# Generated by Django 4.0 on 2022-07-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paystack', '0016_userhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paystack',
            name='generated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
