# Generated by Django 4.1 on 2023-08-17 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_priceincents_order_price_in_cents_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price_in_cents',
            new_name='total_in_cents',
        ),
    ]
