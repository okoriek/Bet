# Generated by Django 4.0 on 2022-03-28 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_games_game_alter_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='result',
            name='date_generated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='KP4yMvyf', max_length=8, null=True, unique=True),
        ),
    ]
