# Generated by Django 5.1 on 2024-09-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_remove_podimages_pod_pods_pod_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="podimages",
            name="image_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]