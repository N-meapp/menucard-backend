# Generated by Django 5.1.1 on 2024-09-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_rename_waiting_menu_items_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tablename',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10),
        ),
    ]
