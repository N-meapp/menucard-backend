# Generated by Django 5.1.1 on 2024-09-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_rename_hide_menu_items_waiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_items',
            name='waiting',
            field=models.CharField(max_length=100),
        ),
    ]
