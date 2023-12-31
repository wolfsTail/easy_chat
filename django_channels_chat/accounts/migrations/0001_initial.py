# Generated by Django 4.2.5 on 2023-09-29 07:11

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Допустимый номер телефона должен быть                                 введён в формате +71234567890 или                                 81234567890', regex='^((\\+7)|8)\\d{10}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
