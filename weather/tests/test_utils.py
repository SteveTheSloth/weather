import pytest
from weather.utils import get_city_data_by_coordinates, get_city_options, create_records, get_forecast_data_by_id, get_current_data_by_id, get_unit_data, create_city_record, create_current_record, create_hourly_records
from weather.models import Weather, City
from weather.tests.data import forecast_data, current_data, city_data


class TestUnits():
    units = ["standard", "metric", "imperial"]
    def test_one(self):
        assert get_unit_data(self.units[0]) == {
                "temp_unit": "K",
                "speed_unit": "meter/s",
            }
    def test_two(self):
        assert get_unit_data(self.units[1]) == {"temp_unit": "C", "speed_unit": "meter/s"}
        
    def test_three(self):
        assert get_unit_data(self.units[2]) == {"temp_unit": "F", "speed_unit": "miles/h"}
    

class TestCurrent():
    city_id = 6548487
    def test_one(self):
        data = get_current_data_by_id(city_id=self.city_id, units="standard")
        assert data.get("id") == self.city_id
        assert data.get("cod") == 200
        
    def test_two(self):
        data = get_current_data_by_id(city_id=self.city_id, units="metric")
        assert data.get("id") == self.city_id
        assert data.get("cod") == 200
    
    def test_three(self):
        data = get_current_data_by_id(city_id=self.city_id, units="imperial")
        assert data.get("id") == self.city_id
        assert data.get("cod") == 200
        
    def test_four(self):
        data = get_current_data_by_id(city_id=0, units="standard")
        assert data.get("cod") == "400"
        assert data.get("message") == "Invalid ID"
        
        
        
class TestForecast():
    city_id = 3333229
    def test_one(self):
        data = get_forecast_data_by_id(city_id=self.city_id, units="standard")
        assert data.get("cod") == "200"
        
    def test_two(self):
        data = get_forecast_data_by_id(city_id=self.city_id, units="metric")
        assert data.get("cod") == "200"
    
    def test_three(self):
        data = get_forecast_data_by_id(city_id=self.city_id, units="imperial")
        assert data.get("cod") == "200"
        
    def test_four(self):
        data = get_forecast_data_by_id(city_id=0, units="standard")
        assert data.get("cod") == "400"
        assert data.get("message") == "Invalid ID"

class TestCoordinates:
    lat = 55.9497
    lon = -3.1933
    def test_one(self):
        data = get_city_data_by_coordinates(lat=self.lat, lon=self.lon, units="metric")
        assert data.get("cod") == 200
        assert data.get("name") == "Edinburgh"
        
    def test_two(self):
        data = get_city_data_by_coordinates(lat=self.lat, lon=self.lon, units="metric")
        assert data.get("cod") == 200
        assert data.get("name") == "Edinburgh"
    
    def test_three(self):
        data = get_city_data_by_coordinates(lat=self.lat, lon=self.lon, units="metric")
        assert data.get("cod") == 200
        assert data.get("name") == "Edinburgh"
    

class TestOptions:
    city = "London"
    country_code = "GB"
    
    def test_one(self):
        data = get_city_options(self.city)
        assert type(data) == type([])
        for option in data:
            assert "name" in option.keys()
            assert "country" in option.keys()
            
    def test_two(self):
        data = get_city_options(self.city, country_code=self.country_code)
        assert type(data) == type([])
        for option in data:
            assert "name" in option.keys()
            assert "country" in option.keys()
            assert option.get("country") == self.country_code
            
    def test_three(self):
        data = get_city_options("qwe")
        assert type(data) == type([])
        assert len(data) == 0
        
@pytest.mark.django_db        
class TestCreateCity():
    data={
                "city_id": 2948052,
                "country": "DE",
                "state": "",
                "name": "Blankenhof",
            }
            
        
    
    def test_one(self):
        create_city_record(self.data)
        assert len(City.objects.filter(city_id=self.data.get("city_id"))) == 1

    def test_two(self):
        create_city_record(self.data)
        create_city_record(self.data)
        assert len(City.objects.filter(city_id=self.data.get("city_id"))) == 1
        
@pytest.mark.django_db        
class TestCreateRecords():
    city_id = 73685
    units = "imperial"
    
   
    def test_one(self):
        create_records(self.city_id, self.units, "")
        
        assert len(Weather.objects.filter(city=self.city_id, current=True)) == 1
        assert len(City.objects.filter(city_id=self.city_id)) == 1
        assert len(Weather.objects.filter(city=self.city_id, current=False)) > 1
    
    
    def test_two(self):
        create_records(6058560, self.units, "Ontario")
        
        assert len(Weather.objects.filter(city=6058560, current=True)) == 1
        assert len(City.objects.filter(city_id=6058560)) == 1
        assert len(Weather.objects.filter(city=6058560, current=False)) > 1
    
   
    def test_three(self):
        create_records(self.city_id, self.units, "")
        create_records(self.city_id, self.units, "")
        
        assert len(Weather.objects.filter(city=self.city_id, current=True)) == 1
        assert len(City.objects.filter(city_id=self.city_id)) == 1
        assert len(Weather.objects.filter(city=self.city_id, current=False)) > 1
        

@pytest.mark.django_db
class TestCreateCurrent():
    data = current_data

    
    def test_one(self):
        create_city_record(city_data)
        create_current_record(self.data)
        assert len(Weather.objects.filter(city=self.data.get("id"), current=True)) == 1
        assert len(Weather.objects.filter(city=self.data.get("id"), current=False)) == 0
    
    def test_two(self):
        create_city_record(city_data)
        create_current_record(self.data)
        create_current_record(self.data)
        assert len(Weather.objects.filter(city=self.data.get("id"), current=True)) == 1
        assert len(Weather.objects.filter(city=self.data.get("id"), current=False)) == 0
        
        

@pytest.mark.django_db
class TestCreateHourly():
    data = forecast_data
    
   
    def test_one(self):
        
        create_hourly_records(self.data)
        assert len(Weather.objects.filter(city=self.data.get("city").get("id"), current=True)) == 0
        assert len(Weather.objects.filter(city=self.data.get("city").get("id"), current=False)) > 1
    
    
    def test_two(self):
        
        create_hourly_records(self.data)
        create_hourly_records(self.data)
        assert len(Weather.objects.filter(city=self.data.get("city").get("id"), current=True)) == 0
        assert len(Weather.objects.filter(city=self.data.get("city").get("id"), current=False)) > 1