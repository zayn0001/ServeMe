# Generated by Django 4.1.5 on 2023-01-21 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10, 'Must have strictly 10 digits')])),
                ('rest_name', models.CharField(max_length=50, null=True)),
                ('branch', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='diner',
            name='email',
        ),
        migrations.AddConstraint(
            model_name='manager',
            constraint=models.UniqueConstraint(fields=('branch', 'rest_name'), name='unique seller'),
        ),
    ]
