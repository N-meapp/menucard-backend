# Generated by Django 5.1.1 on 2024-09-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
