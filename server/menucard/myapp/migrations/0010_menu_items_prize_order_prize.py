# Generated by Django 5.1.1 on 2024-09-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_login_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_items',
            name='prize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='prize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
