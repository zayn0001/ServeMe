# Generated by Django 4.1.5 on 2023-01-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]