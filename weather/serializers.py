from rest_framework import serializers
from .models import Weather, City


class WeatherSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), many=False)

    class Meta:
        model = Weather
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
