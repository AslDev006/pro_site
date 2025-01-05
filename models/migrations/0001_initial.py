# Generated by Django 5.1.3 on 2025-01-05 12:42

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdviceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("phone_number", models.CharField(max_length=13)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("message", models.TextField(blank=True, null=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer_Opinion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("opinion", models.TextField()),
                ("opinion_uz", models.TextField(null=True)),
                ("opinion_en", models.TextField(null=True)),
                ("opinion_ru", models.TextField(null=True)),
                ("full_name", models.CharField(max_length=255)),
                ("full_name_uz", models.CharField(max_length=255, null=True)),
                ("full_name_en", models.CharField(max_length=255, null=True)),
                ("full_name_ru", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="FunctionsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("name_uz", models.CharField(max_length=255, null=True)),
                ("name_en", models.CharField(max_length=255, null=True)),
                ("name_ru", models.CharField(max_length=255, null=True)),
                ("description", models.TextField()),
                ("description_uz", models.TextField(null=True)),
                ("description_en", models.TextField(null=True)),
                ("description_ru", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PartnerModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="partners/")),
                ("name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("position_uz", models.CharField(max_length=255, null=True)),
                ("position_en", models.CharField(max_length=255, null=True)),
                ("position_ru", models.CharField(max_length=255, null=True)),
                ("opinion", models.TextField()),
                ("opinion_uz", models.TextField(null=True)),
                ("opinion_en", models.TextField(null=True)),
                ("opinion_ru", models.TextField(null=True)),
                ("important", models.BooleanField(default=False)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("count", models.IntegerField()),
                ("address", models.CharField(max_length=255)),
                (
                    "feature_count",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(8),
                            django.core.validators.MinValueValidator(3),
                        ]
                    ),
                ),
                ("feature_1", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_2", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_3", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_4", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_5", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_6", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_7", models.CharField(blank=True, max_length=255, null=True)),
                ("feature_8", models.CharField(blank=True, max_length=255, null=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="Services/")),
                ("title", models.CharField(max_length=255)),
                ("title_uz", models.CharField(max_length=255, null=True)),
                ("title_en", models.CharField(max_length=255, null=True)),
                ("title_ru", models.CharField(max_length=255, null=True)),
                ("description", models.TextField()),
                ("description_uz", models.TextField(null=True)),
                ("description_en", models.TextField(null=True)),
                ("description_ru", models.TextField(null=True)),
                ("little_desc", models.TextField()),
                (
                    "currency",
                    models.DecimalField(decimal_places=2, default=200.0, max_digits=7),
                ),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
                ("important", models.BooleanField(default=False)),
            ],
        ),
    ]
