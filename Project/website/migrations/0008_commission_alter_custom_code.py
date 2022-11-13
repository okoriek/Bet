# Generated by Django 4.0 on 2022-11-13 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_custom_bonus_custom_commissions_alter_custom_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('reward', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='custom',
            name='code',
            field=models.CharField(blank=True, default='qCmPtrMV', max_length=8, null=True, unique=True),
        ),
    ]