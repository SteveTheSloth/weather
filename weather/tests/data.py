import datetime

city_data = {"city_id": 73685,
                "country": "YE",
                "state": "",
                "name": "Kilmia"}

forecast_data = {
  "cod": "200",
  "message": 0,
  "cnt": 40,
  "list": [
    {
      "dt": 1706043600,
      "main": {
        "temp": 297.84,
        "feels_like": 298.06,
        "temp_min": 297.67,
        "temp_max": 297.84,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1015,
        "humidity": 65,
        "temp_kf": 0.17
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 18
      },
      "wind": {
        "speed": 7.98,
        "deg": 47,
        "gust": 8.08
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-23 21:00:00"
    },
    {
      "dt": 1706054400,
      "main": {
        "temp": 297.67,
        "feels_like": 297.93,
        "temp_min": 297.55,
        "temp_max": 297.67,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 67,
        "temp_kf": 0.12
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 12
      },
      "wind": {
        "speed": 7.93,
        "deg": 44,
        "gust": 8.07
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-24 00:00:00"
    },
    {
      "dt": 1706065200,
      "main": {
        "temp": 297.62,
        "feels_like": 297.87,
        "temp_min": 297.62,
        "temp_max": 297.62,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1015,
        "humidity": 67,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": {
        "all": 10
      },
      "wind": {
        "speed": 7.05,
        "deg": 50,
        "gust": 7.18
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-24 03:00:00"
    },
    {
      "dt": 1706076000,
      "main": {
        "temp": 297.92,
        "feels_like": 298.18,
        "temp_min": 297.92,
        "temp_max": 297.92,
        "pressure": 1018,
        "sea_level": 1018,
        "grnd_level": 1017,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 11
      },
      "wind": {
        "speed": 7.29,
        "deg": 45,
        "gust": 7.41
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-24 06:00:00"
    },
    {
      "dt": 1706086800,
      "main": {
        "temp": 297.99,
        "feels_like": 298.25,
        "temp_min": 297.99,
        "temp_max": 297.99,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 27
      },
      "wind": {
        "speed": 6.35,
        "deg": 44,
        "gust": 6.39
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-24 09:00:00"
    },
    {
      "dt": 1706097600,
      "main": {
        "temp": 298.21,
        "feels_like": 298.44,
        "temp_min": 298.21,
        "temp_max": 298.21,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 64,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 44
      },
      "wind": {
        "speed": 6.01,
        "deg": 40,
        "gust": 5.88
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-24 12:00:00"
    },
    {
      "dt": 1706108400,
      "main": {
        "temp": 298.02,
        "feels_like": 298.29,
        "temp_min": 298.02,
        "temp_max": 298.02,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 78
      },
      "wind": {
        "speed": 5.65,
        "deg": 39,
        "gust": 5.61
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-24 15:00:00"
    },
    {
      "dt": 1706119200,
      "main": {
        "temp": 298.08,
        "feels_like": 298.38,
        "temp_min": 298.08,
        "temp_max": 298.08,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1015,
        "humidity": 67,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 78
      },
      "wind": {
        "speed": 6.53,
        "deg": 39,
        "gust": 6.4
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-24 18:00:00"
    },
    {
      "dt": 1706130000,
      "main": {
        "temp": 297.93,
        "feels_like": 298.27,
        "temp_min": 297.93,
        "temp_max": 297.93,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1014,
        "humidity": 69,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 66
      },
      "wind": {
        "speed": 6.66,
        "deg": 46,
        "gust": 6.66
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-24 21:00:00"
    },
    {
      "dt": 1706140800,
      "main": {
        "temp": 297.88,
        "feels_like": 298.13,
        "temp_min": 297.88,
        "temp_max": 297.88,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1013,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 83
      },
      "wind": {
        "speed": 3.98,
        "deg": 83,
        "gust": 3.94
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-25 00:00:00"
    },
    {
      "dt": 1706151600,
      "main": {
        "temp": 297.81,
        "feels_like": 297.98,
        "temp_min": 297.81,
        "temp_max": 297.81,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1015,
        "humidity": 63,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 99
      },
      "wind": {
        "speed": 4.19,
        "deg": 53,
        "gust": 3.5
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-25 03:00:00"
    },
    {
      "dt": 1706162400,
      "main": {
        "temp": 297.58,
        "feels_like": 297.75,
        "temp_min": 297.58,
        "temp_max": 297.58,
        "pressure": 1018,
        "sea_level": 1018,
        "grnd_level": 1016,
        "humidity": 64,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 84
      },
      "wind": {
        "speed": 4.34,
        "deg": 48,
        "gust": 4.35
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-25 06:00:00"
    },
    {
      "dt": 1706173200,
      "main": {
        "temp": 297.77,
        "feels_like": 297.98,
        "temp_min": 297.77,
        "temp_max": 297.77,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 65,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 38
      },
      "wind": {
        "speed": 4.62,
        "deg": 42,
        "gust": 4.58
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-25 09:00:00"
    },
    {
      "dt": 1706184000,
      "main": {
        "temp": 297.71,
        "feels_like": 297.94,
        "temp_min": 297.71,
        "temp_max": 297.71,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 36
      },
      "wind": {
        "speed": 4.27,
        "deg": 50,
        "gust": 4.22
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-25 12:00:00"
    },
    {
      "dt": 1706194800,
      "main": {
        "temp": 297.66,
        "feels_like": 297.92,
        "temp_min": 297.66,
        "temp_max": 297.66,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 67,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 76
      },
      "wind": {
        "speed": 3.77,
        "deg": 58,
        "gust": 3.74
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-25 15:00:00"
    },
    {
      "dt": 1706205600,
      "main": {
        "temp": 297.49,
        "feels_like": 297.73,
        "temp_min": 297.49,
        "temp_max": 297.49,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1015,
        "humidity": 67,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 77
      },
      "wind": {
        "speed": 3.72,
        "deg": 59,
        "gust": 3.67
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-25 18:00:00"
    },
    {
      "dt": 1706216400,
      "main": {
        "temp": 297.28,
        "feels_like": 297.55,
        "temp_min": 297.28,
        "temp_max": 297.28,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1013,
        "humidity": 69,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 33
      },
      "wind": {
        "speed": 4.17,
        "deg": 62,
        "gust": 4.06
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-25 21:00:00"
    },
    {
      "dt": 1706227200,
      "main": {
        "temp": 297.36,
        "feels_like": 297.56,
        "temp_min": 297.36,
        "temp_max": 297.36,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 66,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 44
      },
      "wind": {
        "speed": 3.08,
        "deg": 48,
        "gust": 3.2
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-26 00:00:00"
    },
    {
      "dt": 1706238000,
      "main": {
        "temp": 297.71,
        "feels_like": 297.89,
        "temp_min": 297.71,
        "temp_max": 297.71,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 64,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 42
      },
      "wind": {
        "speed": 3.3,
        "deg": 104,
        "gust": 3
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-26 03:00:00"
    },
    {
      "dt": 1706248800,
      "main": {
        "temp": 297.48,
        "feels_like": 297.77,
        "temp_min": 297.48,
        "temp_max": 297.48,
        "pressure": 1018,
        "sea_level": 1018,
        "grnd_level": 1016,
        "humidity": 69,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 24
      },
      "wind": {
        "speed": 3.85,
        "deg": 133,
        "gust": 4.27
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-26 06:00:00"
    },
    {
      "dt": 1706259600,
      "main": {
        "temp": 297.99,
        "feels_like": 298.23,
        "temp_min": 297.99,
        "temp_max": 297.99,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 65,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 29
      },
      "wind": {
        "speed": 2.69,
        "deg": 135,
        "gust": 2.83
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-26 09:00:00"
    },
    {
      "dt": 1706270400,
      "main": {
        "temp": 298.1,
        "feels_like": 298.35,
        "temp_min": 298.1,
        "temp_max": 298.1,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 65,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 28
      },
      "wind": {
        "speed": 2.81,
        "deg": 137,
        "gust": 3
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-26 12:00:00"
    },
    {
      "dt": 1706281200,
      "main": {
        "temp": 298.17,
        "feels_like": 298.53,
        "temp_min": 298.17,
        "temp_max": 298.17,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 69,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": {
        "all": 7
      },
      "wind": {
        "speed": 4.67,
        "deg": 129,
        "gust": 4.77
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-26 15:00:00"
    },
    {
      "dt": 1706292000,
      "main": {
        "temp": 298.14,
        "feels_like": 298.55,
        "temp_min": 298.14,
        "temp_max": 298.14,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1014,
        "humidity": 71,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 17
      },
      "wind": {
        "speed": 5.4,
        "deg": 131,
        "gust": 5.59
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-26 18:00:00"
    },
    {
      "dt": 1706302800,
      "main": {
        "temp": 298.08,
        "feels_like": 298.46,
        "temp_min": 298.08,
        "temp_max": 298.08,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1013,
        "humidity": 70,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 16
      },
      "wind": {
        "speed": 3.1,
        "deg": 133,
        "gust": 3.61
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-26 21:00:00"
    },
    {
      "dt": 1706313600,
      "main": {
        "temp": 297.89,
        "feels_like": 298.25,
        "temp_min": 297.89,
        "temp_max": 297.89,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1012,
        "humidity": 70,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 14
      },
      "wind": {
        "speed": 1.9,
        "deg": 85,
        "gust": 2
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-27 00:00:00"
    },
    {
      "dt": 1706324400,
      "main": {
        "temp": 297.93,
        "feels_like": 298.34,
        "temp_min": 297.93,
        "temp_max": 297.93,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1013,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 58
      },
      "wind": {
        "speed": 2.97,
        "deg": 94,
        "gust": 3.04
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-27 03:00:00"
    },
    {
      "dt": 1706335200,
      "main": {
        "temp": 298.16,
        "feels_like": 298.6,
        "temp_min": 298.16,
        "temp_max": 298.16,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1015,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 47
      },
      "wind": {
        "speed": 3.31,
        "deg": 112,
        "gust": 3.36
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-27 06:00:00"
    },
    {
      "dt": 1706346000,
      "main": {
        "temp": 298.32,
        "feels_like": 298.77,
        "temp_min": 298.32,
        "temp_max": 298.32,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1013,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 81
      },
      "wind": {
        "speed": 2.75,
        "deg": 117,
        "gust": 2.92
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-27 09:00:00"
    },
    {
      "dt": 1706356800,
      "main": {
        "temp": 298.41,
        "feels_like": 298.85,
        "temp_min": 298.41,
        "temp_max": 298.41,
        "pressure": 1013,
        "sea_level": 1013,
        "grnd_level": 1011,
        "humidity": 71,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 77
      },
      "wind": {
        "speed": 1.61,
        "deg": 108,
        "gust": 1.66
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-27 12:00:00"
    },
    {
      "dt": 1706367600,
      "main": {
        "temp": 298.47,
        "feels_like": 298.94,
        "temp_min": 298.47,
        "temp_max": 298.47,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1013,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 71
      },
      "wind": {
        "speed": 2.14,
        "deg": 77,
        "gust": 1.99
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-27 15:00:00"
    },
    {
      "dt": 1706378400,
      "main": {
        "temp": 298.39,
        "feels_like": 298.85,
        "temp_min": 298.39,
        "temp_max": 298.39,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 62
      },
      "wind": {
        "speed": 1.94,
        "deg": 74,
        "gust": 1.91
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-27 18:00:00"
    },
    {
      "dt": 1706389200,
      "main": {
        "temp": 298.14,
        "feels_like": 298.6,
        "temp_min": 298.14,
        "temp_max": 298.14,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 40
      },
      "wind": {
        "speed": 2.01,
        "deg": 44,
        "gust": 1.87
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-27 21:00:00"
    },
    {
      "dt": 1706400000,
      "main": {
        "temp": 297.84,
        "feels_like": 298.32,
        "temp_min": 297.84,
        "temp_max": 297.84,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1013,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 28
      },
      "wind": {
        "speed": 2.5,
        "deg": 40,
        "gust": 2.26
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-28 00:00:00"
    },
    {
      "dt": 1706410800,
      "main": {
        "temp": 297.8,
        "feels_like": 298.28,
        "temp_min": 297.8,
        "temp_max": 297.8,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 36
      },
      "wind": {
        "speed": 2.44,
        "deg": 60,
        "gust": 2.26
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-28 03:00:00"
    },
    {
      "dt": 1706421600,
      "main": {
        "temp": 297.92,
        "feels_like": 298.38,
        "temp_min": 297.92,
        "temp_max": 297.92,
        "pressure": 1017,
        "sea_level": 1017,
        "grnd_level": 1016,
        "humidity": 74,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 28
      },
      "wind": {
        "speed": 2.29,
        "deg": 57,
        "gust": 2.21
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-28 06:00:00"
    },
    {
      "dt": 1706432400,
      "main": {
        "temp": 298.08,
        "feels_like": 298.53,
        "temp_min": 298.08,
        "temp_max": 298.08,
        "pressure": 1016,
        "sea_level": 1016,
        "grnd_level": 1014,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 14
      },
      "wind": {
        "speed": 3.06,
        "deg": 20,
        "gust": 2.95
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-28 09:00:00"
    },
    {
      "dt": 1706443200,
      "main": {
        "temp": 298.15,
        "feels_like": 298.59,
        "temp_min": 298.15,
        "temp_max": 298.15,
        "pressure": 1013,
        "sea_level": 1013,
        "grnd_level": 1012,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 17
      },
      "wind": {
        "speed": 3.13,
        "deg": 20,
        "gust": 3.16
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-01-28 12:00:00"
    },
    {
      "dt": 1706454000,
      "main": {
        "temp": 298.16,
        "feels_like": 298.62,
        "temp_min": 298.16,
        "temp_max": 298.16,
        "pressure": 1014,
        "sea_level": 1014,
        "grnd_level": 1013,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 22
      },
      "wind": {
        "speed": 4.12,
        "deg": 28,
        "gust": 4.2
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-28 15:00:00"
    },
    {
      "dt": 1706464800,
      "main": {
        "temp": 298.17,
        "feels_like": 298.69,
        "temp_min": 298.17,
        "temp_max": 298.17,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 1014,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 32
      },
      "wind": {
        "speed": 5.71,
        "deg": 39,
        "gust": 5.97
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-01-28 18:00:00"
    }
  ],
  "city": {
    "id": 73685,
    "name": "Kilmia",
    "coord": {
      "lat": 12.1858,
      "lon": 52.2333
    },
    "country": "YE",
    "population": 0,
    "timezone": 10800,
    "sunrise": 1705978593,
    "sunset": 1706020110,
  },
  "temp_unit": "C",
  "speed_unit": "meter/s",
  
}

current_data = {
  "coord": {
    "lon": 52.2333,
    "lat": 12.1858
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 297.82,
    "feels_like": 298.04,
    "temp_min": 297.82,
    "temp_max": 297.82,
    "pressure": 1017,
    "humidity": 65,
    "sea_level": 1017,
    "grnd_level": 1016
  },
  "visibility": 10000,
  "wind": {
    "speed": 8.61,
    "deg": 45,
    "gust": 8.8
  },
  "clouds": {
    "all": 11
  },
  "dt": 1706035716,
  "sys": {
    "country": "YE",
    "sunrise": 1705978593,
    "sunset": 1706020110
  },
  "timezone": 10800,
  "id": 73685,
  "name": "Kilmia",
  "cod": 200,
  "temp_unit": "C",
  "speed_unit": "meter/s",
  "current": True
}

weather_model_data = {'city': 73685, 'feels_like': 298.04, 'wind_gust': 8.8, 'weather': 'Clouds', 'icon': '02n', 'temperature': 297.82, 'pressure': 1017, 'humidity': 65, 'wind_speed': 8.61, 'wind_direction': 45, 'clouds': 11, 'current': True, 'date_time': datetime.datetime.now(), 'temp_unit': 'C', 'speed_unit': 'meter/s'}