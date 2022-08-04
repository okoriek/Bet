# Generated by Django 4.0 on 2022-07-23 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flutterwave', '0003_alter_flutterwave_generated'),
        ('paystack', '0015_remove_paystack_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('amount', models.CharField(blank=True, max_length=30, null=True)),
                ('transaction', models.CharField(blank=True, choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=20, null=True)),
                ('confirm', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField()),
                ('flutterwave', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flutterwave.flutterwave')),
                ('paystack', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paystack.paystack')),
            ],
            options={
                'verbose_name_plural': 'User Histories',
                'ordering': ('-date_created',),
            },
        ),
    ]
