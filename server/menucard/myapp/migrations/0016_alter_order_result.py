# Generated by Django 5.1.1 on 2024-09-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_status_order_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='result',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
