# Generated by Django 5.1.4 on 2025-01-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='amount_to',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='card',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='code',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='passport',
        ),
    ]
