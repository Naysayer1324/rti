# Generated by Django 5.1.2 on 2024-10-31 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_categories_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория'),
        ),
    ]