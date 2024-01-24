# Generated by Django 5.0.1 on 2024-01-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CityWeather",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("weather", models.CharField(max_length=50)),
                ("icon", models.CharField(max_length=6)),
                ("temperature", models.FloatField(max_length=6)),
                ("feels_like", models.FloatField(blank=True, max_length=6, null=True)),
                ("pressure", models.IntegerField(blank=True, null=True)),
                ("humidity", models.IntegerField(blank=True, null=True)),
                ("wind_speed", models.FloatField(blank=True, max_length=6, null=True)),
                ("wind_direction", models.IntegerField(blank=True, null=True)),
                ("wind_gust", models.FloatField(blank=True, max_length=6, null=True)),
                ("clouds", models.IntegerField(blank=True, null=True)),
                ("country", models.CharField(max_length=2)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("name", models.CharField(max_length=50)),
                ("temp_unit", models.CharField(max_length=6)),
                ("speed_unit", models.CharField(max_length=6)),
            ],
        ),
    ]
