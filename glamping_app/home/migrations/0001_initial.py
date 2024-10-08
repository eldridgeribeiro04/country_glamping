# Generated by Django 4.1.7 on 2024-08-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pods",
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
                ("name", models.CharField(max_length=200)),
                ("max_occupancy", models.IntegerField(default=1)),
                ("beds", models.IntegerField(default=0)),
                ("washrooms", models.IntegerField(default=0)),
                ("height", models.IntegerField(default=0)),
                ("width", models.IntegerField(default=0)),
                ("price", models.DecimalField(decimal_places=2, max_digits=3)),
                (
                    "images",
                    models.ImageField(blank=True, null=True, upload_to="pod_images/"),
                ),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("description", models.TextField()),
            ],
        ),
    ]
