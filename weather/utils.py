import requests

from weather_app.secrets import API_KEY
from .models import City, Weather
from .serializers import CitySerializer, WeatherSerializer
import datetime

base_url = "http://api.openweathermap.org/"


def get_city_options(city, country_code=""):
    """Make api call to get up to 5 city options to choose from."""

    if country_code:
        country_code = "," + country_code
    options_url = (
        base_url
        + "geo/1.0/direct?q={city}{country_code}&limit=5&appid={key}".format(
            city=city, country_code=country_code, key=API_KEY
        )
    )
    return requests.get(options_url).json()


def get_city_data_by_coordinates(lat, lon, units=""):
    """Make api call to get weather data for one city."""

    url = (
        base_url
        + "data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units={units}".format(
            lat=lat, lon=lon, key=API_KEY, units=units
        )
    )
    return requests.get(url).json()


def get_forecast_data_by_id(city_id, units=""):
    """Make api call to get weather forecast data based on city_id."""

    url = base_url + "data/2.5/forecast?id={city_id}&appid={key}&units={units}".format(
        city_id=city_id, key=API_KEY, units=units
    )
    return requests.get(url).json()


def get_current_data_by_id(city_id, units=""):
    """Make api call to get current weather data based on city_id."""

    url = base_url + "data/2.5/weather?id={city_id}&appid={key}&units={units}".format(
        city_id=city_id, key=API_KEY, units=units
    )
    return requests.get(url).json()


def get_unit_data(units):
    """Create unit_data dictionary based on user selected units."""

    if units == "standard":
        unit_data = {
            "temp_unit": "K",
            "speed_unit": "meter/s",
        }
    elif units == "metric":
        unit_data = {"temp_unit": "C", "speed_unit": "meter/s"}
    else:
        unit_data = {"temp_unit": "F", "speed_unit": "miles/h"}

    return unit_data


def create_records(city_id, units, state):
    """Call API functions to get data, manipulate data and call functions to create records."""

    data = get_forecast_data_by_id(city_id=city_id, units=units)
    data.update(unit_data := get_unit_data(units=units))
    data["state"] = state
    create_hourly_records(data)

    data = get_current_data_by_id(city_id=city_id, units=units)
    data.update(unit_data)
    create_current_record(data)


def create_city_record(data):
    """Create city record if it doesn't already exist."""

    try:
        City.objects.get(city_id=data.get("id"))
    except City.DoesNotExist:
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()


def create_current_record(data):
    """Create record for current weather data."""

    data = {
        "city": data.get("id"),
        "feels_like": data.get("main").get("feels_like"),
        "wind_gust": data.get("wind").get("gust"),
        "weather": data.get("weather")[0].get("main"),
        "icon": data.get("weather")[0].get("icon"),
        "temperature": data.get("main").get("temp"),
        "pressure": data.get("main").get("pressure"),
        "humidity": data.get("main").get("humidity"),
        "wind_speed": data.get("wind").get("speed"),
        "wind_direction": data.get("wind").get("deg"),
        "clouds": data.get("clouds").get("all"),
        "current": True,
        "date_time": datetime.datetime.fromtimestamp(data.get("dt")),
        "temp_unit": data.get("temp_unit"),
        "speed_unit": data.get("speed_unit"),
    }

    try:  # If record for current weather already exists, update. Else create new record.
        record = Weather.objects.get(city=data.get("city"), current=True)
        serializer = WeatherSerializer(record, data=data)

    except Weather.DoesNotExist:
        serializer = WeatherSerializer(data=data)
    if serializer.is_valid():
        serializer.save()


def create_hourly_records(data):
    """Create Weather records from forecast data."""

    try:  # If City record does not yet exits, create
        City.objects.get(city_id=data.get("city").get("id"))
    except City.DoesNotExist:
        create_city_record(
            data={
                "city_id": data.get("city").get("id"),
                "country": data.get("city").get("country"),
                "state": data.get("state"),
                "name": data.get("city").get("name"),
            }
        )

    try:  # Delete records to make sure data is up to date.
        records = Weather.objects.filter(
            city=data.get("list")[0].get("id"), current=False
        )
        records.delete()
        
    except Weather.DoesNotExist:
        pass

    for item in data.get("list"):
        hour_data = {
            "date_time": datetime.datetime.fromtimestamp(item.get("dt")),
            "city": data.get("city").get("id"),
            "weather": item.get("weather")[0].get("main"),
            "icon": item.get("weather")[0].get("icon"),
            "feels_like": item.get("main").get("feels_like"),
            "temperature": item.get("main").get("temp"),
            "pressure": item.get("main").get("pressure"),
            "humidity": item.get("main").get("humidity"),
            "wind_speed": item.get("wind").get("speed"),
            "wind_direction": item.get("wind").get("deg"),
            "wind_gust": item.get("wind").get("gust"),
            "clouds": item.get("clouds").get("all"),
            "current": False,
            "temp_unit": data.get("temp_unit"),
            "speed_unit": data.get("speed_unit"),
        }

        serializer = WeatherSerializer(data=hour_data)
        if serializer.is_valid():
            serializer.save()
