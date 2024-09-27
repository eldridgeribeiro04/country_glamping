# Generated by Django 5.1 on 2024-09-27 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_podimages_image_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pods",
            name="pod_images",
        ),
        migrations.AddField(
            model_name="pods",
            name="pod_images",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pod_images",
                to="home.podimages",
            ),
        ),
    ]