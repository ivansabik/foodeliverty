# Generated by Django 3.2.10 on 2023-11-08 03:26

from django.db import migrations, models
import django_enumfield.db.fields
import bouffet.orders.models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('cancel_reason', models.TextField(blank=True, null=True)),
                ('cancelled_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_appt_unit_suite_number_floor', models.CharField(blank=True, max_length=10, null=True)),
                ('delivery_city', models.CharField(max_length=100)),
                ('delivery_contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('delivery_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('delivery_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('delivery_lon', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('delivery_notes', models.TextField(blank=True, null=True)),
                ('delivery_state_province', models.CharField(max_length=100)),
                ('delivery_street_address', models.CharField(max_length=100)),
                ('delivery_zip_code', models.CharField(max_length=10)),
                ('fulfilled_at', models.DateTimeField(blank=True, null=True)),
                ('fulfillment_type', django_enumfield.db.fields.EnumField(enum=bouffet.orders.models.OrderFulfillmentType)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('ready_for_fulfillment_at', models.DateTimeField(blank=True, null=True)),
                ('reject_reason', models.TextField(blank=True, null=True)),
                ('rejected_at', models.DateTimeField(blank=True, null=True)),
                ('share_url', models.URLField(blank=True, null=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=bouffet.orders.models.OrderStatus)),
                ('total_order_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('selected_option', models.CharField(blank=True, max_length=50, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('children_items', models.ManyToManyField(blank=True, to='orders.OrderItem')),
            ],
        ),
    ]
