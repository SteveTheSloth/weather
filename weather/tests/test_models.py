from weather.models import Weather, City
from weather.tests.data import weather_model_data, city_data
from weather.utils import create_records
from datetime import datetime, timedelta
import pytest
from django.db.utils import IntegrityError
    
@pytest.mark.django_db
class TestCity():

    def test_one(self):
        City.objects.create(**city_data)
        assert len(City.objects.filter(city_id=city_data.get("city_id"))) == 1
 
    def test_two(self):
        city = City.objects.create(**city_data)
        current_weather = Weather.objects.create(city=city, **{k: v for k, v in weather_model_data.items() if k!= "city"})
        assert city.get_current_data() == current_weather
   
    def test_three(self):
        city = City.objects.create(**city_data)
        create_records(city.city_id, "standard", "")
        daily_data = city.get_daily_data()
        tomorrow = datetime.now().date() + timedelta(days=1)
        assert daily_data[0].get("date") == tomorrow
        tomorrow_weather = Weather.objects.filter(city=city.city_id, current=False, date_time__date=tomorrow)
        max_temp = 0
        min_temp = tomorrow_weather[0].temperature
        for i in tomorrow_weather:
            if i.temperature > max_temp:
                max_temp = i.temperature
            if i.temperature < min_temp:
                min_temp = i.temperature
                
        assert daily_data[0].get("temperature__max") == max_temp
        assert daily_data[0].get("temperature__min") == min_temp
        
@pytest.mark.django_db
class TestWeather():
    
    def test_one(self):
        city_entry = City.objects.create(**city_data)
        weather_entry = Weather.objects.create(city=city_entry, **{k: v for k, v in weather_model_data.items() if k!= "city"})
        
        assert weather_entry == city_entry.city_weather.get(current=True)
        assert weather_entry.city == city_entry
        
    def test_two(self):
        with pytest.raises(IntegrityError):
            city_entry = City.objects.create(**city_data)
            weather_entry = Weather.objects.create(city=city_entry, **{k: v for k, v in weather_model_data.items() if k!= "city"})
            weather_entry_two = Weather.objects.create(city=city_entry, **{k: v for k, v in weather_model_data.items() if k!= "city"})
            