# Generated by Django 4.0 on 2022-11-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_commission_alter_custom_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='code',
            field=models.CharField(blank=True, default='LU0ZN7AJ', max_length=8, null=True, unique=True),
        ),
    ]
