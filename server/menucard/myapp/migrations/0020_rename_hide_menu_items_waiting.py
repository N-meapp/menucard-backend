# Generated by Django 5.1.1 on 2024-09-17 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_menu_items_hide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu_items',
            old_name='hide',
            new_name='waiting',
        ),
    ]
