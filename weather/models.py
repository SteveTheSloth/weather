from django.db import models
from datetime import datetime, timedelta
from django.db.models import Max, Min, Q
from django.db.models.constraints import UniqueConstraint


class City(models.Model):
    class Meta:
        verbose_name = "City data"
        verbose_name_plural = "City data"

    city_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=2)
    state = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)

    def get_daily_data(self):
        """Collect and aggregate weather data data to show in forecast."""

        date = datetime.now().date() + timedelta(days=1)
        daily_data = []
        end_date = date + timedelta(days=4)
        while date <= end_date:
            queryset = self.city_weather.filter(date_time__date=date)

            day = queryset.aggregate(Max("temperature"))
            day.update(queryset.aggregate(Min("temperature")))
            day.update(queryset.aggregate(Max("wind_speed")))
            day.update(queryset.aggregate(Min("wind_speed")))
            day["date"] = date
            date += timedelta(days=1)
            daily_data.append(day)
        print(daily_data)
        return daily_data

    def get_current_data(self):
        """Get Weather instance containing the curent weather data."""

        return self.city_weather.get(current=True)

    def __str__(self):
        if self.state:
            return self.name + ", " + self.state + ", " + self.country

        return self.name + ", " + self.country


class Weather(models.Model):
    weather = models.CharField(max_length=50)
    icon = models.CharField(max_length=6)
    temperature = models.FloatField(max_length=6)
    feels_like = models.FloatField(max_length=6, blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)
    wind_speed = models.FloatField(max_length=6, blank=True, null=True)
    wind_direction = models.IntegerField(blank=True, null=True)
    wind_gust = models.FloatField(max_length=6, blank=True, null=True)
    clouds = models.IntegerField(blank=True, null=True)
    temp_unit = models.CharField(max_length=30)
    speed_unit = models.CharField(max_length=30)
    current = models.BooleanField(
        default=False,
        help_text="Field representing if record represents current weather or forecast data",
    )
    date_time = models.DateTimeField()
    city = models.ForeignKey(
        City, related_name="city_weather", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Weather Data"
        verbose_name_plural = "Weather Data"
        constraints = [
            UniqueConstraint(
                fields=["city"], condition=Q(current=True), name="unique_current_true"
            ),
        ]

    def __str__(self):
        return (
            "Weather for "
            + self.city.name
            + " at: "
            + self.date_time.strftime("%d/%m/%Y, %H:%M:%S")
        )
