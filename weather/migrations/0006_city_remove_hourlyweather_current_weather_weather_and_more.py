# Generated by Django 5.0.1 on 2024-01-20 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0005_remove_hourlyweather_currentweather_ptr_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("city_id", models.IntegerField(primary_key=True, serialize=False)),
                ("country", models.CharField(max_length=2)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Current weather data",
                "verbose_name_plural": "Current weather data",
            },
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
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
                ("temp_unit", models.CharField(max_length=30)),
                ("speed_unit", models.CharField(max_length=30)),
                ("current", models.BooleanField(default=False)),
                ("date_time", models.DateTimeField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city_weather",
                        to="weather.city",
                    ),
                ),
            ],
            options={
                "verbose_name": "Weather Data",
                "verbose_name_plural": "Weather Data",
            },
        ),
    ]
