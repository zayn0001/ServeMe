# Generated by Django 4.1.5 on 2023-01-21 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_manager_remove_diner_email_manager_unique seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=1000)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.manager')),
            ],
        ),
    ]
