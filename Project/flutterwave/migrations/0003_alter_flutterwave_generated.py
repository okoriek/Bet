# Generated by Django 4.0 on 2022-07-17 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flutterwave', '0002_alter_flutterwave_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutterwave',
            name='generated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
