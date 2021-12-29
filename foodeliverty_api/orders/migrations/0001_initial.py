# Generated by Django 3.2.10 on 2021-12-29 01:55

import uuid

import django.db.models.deletion
import django_enumfield.db.fields
import phonenumber_field.modelfields
import taggit.managers
from django.db import migrations, models

import foodeliverty_api.orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stores", "0001_initial"),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryCourier",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("last_name", models.CharField(max_length=50)),
                ("phone_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
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
            name="Order",
            fields=[
                ("cancel_reason", models.TextField()),
                ("cancelled_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("delivery_appt_suite_number", models.CharField(max_length=10)),
                ("delivery_city", models.CharField(max_length=100)),
                ("delivery_contact_phone", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ("delivery_fee", models.DecimalField(decimal_places=2, max_digits=6)),
                ("delivery_lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("delivery_lon", models.DecimalField(decimal_places=6, max_digits=9)),
                ("delivery_notes", models.TextField()),
                ("delivery_street_address", models.CharField(max_length=100)),
                ("delivery_zip_code", models.CharField(max_length=10)),
                ("fulfilled_at", models.DateTimeField(blank=True, null=True)),
                (
                    "fulfillment_type",
                    django_enumfield.db.fields.EnumField(enum=foodeliverty_api.orders.models.OrderFulfillmentType),
                ),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("notes", models.TextField()),
                ("paid_at", models.DateTimeField(blank=True, null=True)),
                ("ready_for_fulfillment_at", models.DateTimeField(blank=True, null=True)),
                ("reject_reason", models.TextField()),
                ("rejected_at", models.DateTimeField(blank=True, null=True)),
                ("share_url", models.URLField(blank=True, null=True)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    django_enumfield.db.fields.EnumField(default=0, enum=foodeliverty_api.orders.models.OrderStatus),
                ),
                ("tip_amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("total_order_amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
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
                (
                    "delivery_courier",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="orders.deliverycourier"
                    ),
                ),
                ("menu_items", models.ManyToManyField(to="stores.MenuItem")),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryTrackingPoint",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="orders.order"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("email", models.EmailField(max_length=100)),
                ("email_verified", models.BooleanField(default=False)),
                ("first_name", models.CharField(max_length=50)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("last_name", models.CharField(max_length=50)),
                ("phone_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ("phone_number_verified", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
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
    ]
