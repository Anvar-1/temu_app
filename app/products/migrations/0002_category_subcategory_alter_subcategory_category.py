# Generated by Django 5.1.4 on 2025-01-17 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ManyToManyField(blank=True, related_name='categories', to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_set', to='products.category'),
        ),
    ]
