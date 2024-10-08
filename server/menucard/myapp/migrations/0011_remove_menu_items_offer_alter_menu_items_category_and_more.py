# Generated by Django 5.1.1 on 2024-09-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_menu_items_prize_order_prize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_items',
            name='Offer',
        ),
        migrations.AlterField(
            model_name='menu_items',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu_items',
            name='prize',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='menu_items',
            name='offer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
