# Generated by Django 5.1.4 on 2025-01-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_api', '0002_remove_offer_amount_to_remove_offer_card_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='offer',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
