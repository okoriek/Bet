# Generated by Django 4.0 on 2022-07-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_user_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userhistory',
            options={'ordering': ('-date_created',), 'verbose_name_plural': 'User Histories'},
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='2VvXMlMb', max_length=8, null=True, unique=True),
        ),
    ]