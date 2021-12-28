# Generated by Django 3.2.10 on 2021-12-28 23:28

import uuid

import django.core.validators
import django.db.models.deletion
import django_enumfield.db.fields
import phonenumber_field.modelfields
import taggit.managers
from django.db import migrations, models

import foodeliverty_api.stores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="Holiday",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "day",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(31),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("holiday_name", models.CharField(max_length=50)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "month",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(12),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="MenuCategory",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField()),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("image_url", models.URLField(blank=True, null=True)),
                ("name", models.CharField(max_length=50)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("available", models.BooleanField(default=True)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField()),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("image_url", models.URLField(blank=True, null=True)),
                (
                    "item_type",
                    django_enumfield.db.fields.EnumField(default=0, enum=foodeliverty_api.stores.models.MenuItemType),
                ),
                ("name", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("sku", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="stores.menucategory"
                    ),
                ),
                (
                    "custom_labels",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OpeningHour",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "day",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(31),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("end_time", models.TimeField()),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("start_time", models.TimeField()),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                ("city", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("currency", models.CharField(max_length=3)),
                ("delivery_fee", models.DecimalField(decimal_places=2, max_digits=6)),
                ("delivery_menu_url", models.URLField(blank=True, null=True)),
                ("delivery_radius_km", models.DecimalField(decimal_places=2, max_digits=6)),
                ("fullfills_delivery", models.BooleanField(default=True)),
                ("fullfills_pickup", models.BooleanField(default=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("image_url", models.URLField(blank=True, null=True)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9)),
                ("name", models.CharField(max_length=20)),
                ("phone_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ("street_address", models.CharField(max_length=100)),
                ("street_number", models.IntegerField()),
                ("timezone", models.CharField(blank=True, max_length=50, null=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("zip_code", models.CharField(max_length=10)),
                (
                    "custom_labels",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                ("holidays", models.ManyToManyField(to="stores.Holiday")),
                ("menu_items", models.ManyToManyField(to="stores.MenuItem")),
                ("opening_hours", models.ManyToManyField(to="stores.OpeningHour")),
            ],
        ),
    ]
