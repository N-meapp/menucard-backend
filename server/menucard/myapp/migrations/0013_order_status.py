# Generated by Django 5.1.1 on 2024-09-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
