# Generated by Django 5.1.1 on 2024-09-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_items',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='Category_image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
