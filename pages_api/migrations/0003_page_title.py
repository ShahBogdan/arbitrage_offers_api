# Generated by Django 5.1.4 on 2025-01-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_api', '0002_alter_page_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='NEW PAGE', max_length=255, verbose_name='Назва'),
        ),
    ]
