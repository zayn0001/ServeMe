# Generated by Django 4.1.5 on 2023-01-22 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_remove_layout_numcols_remove_layout_numrows_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menudata',
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.menu')),
            ],
        ),
    ]
