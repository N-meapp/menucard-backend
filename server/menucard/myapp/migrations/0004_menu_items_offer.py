# Generated by Django 5.1.1 on 2024-09-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_items',
            name='Offer',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
