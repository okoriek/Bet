# Generated by Django 4.0 on 2022-07-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='vKHoTcnn', max_length=8, null=True, unique=True),
        ),
    ]