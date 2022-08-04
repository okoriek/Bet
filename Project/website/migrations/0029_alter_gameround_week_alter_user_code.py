# Generated by Django 4.0 on 2022-07-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_game_week_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameround',
            name='week',
            field=models.CharField(blank=True, max_length=10000000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='8sXGFKj7', max_length=8, null=True, unique=True),
        ),
    ]
