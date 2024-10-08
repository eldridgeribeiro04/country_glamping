# Generated by Django 5.1 on 2024-09-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0005_remove_booking_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("available", "Available"),
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("cancelled", "Cancelled"),
                    ("arrived", "Arrived"),
                    ("departed", "Departed"),
                    ("completed", "Completed"),
                ],
                default="available",
                max_length=10,
            ),
        ),
    ]
