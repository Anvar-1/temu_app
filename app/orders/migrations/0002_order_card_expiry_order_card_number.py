# Generated by Django 5.1.4 on 2025-01-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card_expiry',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]