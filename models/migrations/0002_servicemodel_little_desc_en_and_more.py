# Generated by Django 5.1.3 on 2025-01-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicemodel",
            name="little_desc_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="servicemodel",
            name="little_desc_ru",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="servicemodel",
            name="little_desc_uz",
            field=models.TextField(null=True),
        ),
    ]
