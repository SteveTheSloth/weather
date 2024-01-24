# Display Weather data for desired location with Django / HTML / CSS

This application makes api-calls to the openweathermap.org api based on user input, converts the response into a database entry, and shows weather data for the desired location on a seperate details page.

It is built using Django, as well as HTML and CSS.

## Installation

To test functionality, clone repository, create a virtual environment and install dependencies.

Create a file named **secrets.py** in the weather_app directory. This file should contain two variables called **SECRET_KEY** and **API_KEY** which store your secret key and your api key in string format (with quotation marks).

Run **python manage.py migrate** to apply migrations & create database.

Run **python manage.py runserver** to start app on local server.

```bash
pipenv shell
pipenv install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

The application should now be running on your local server at http://127.0.0.1:8000 (or on port specified by **python manage.py runserver** command). You can now search for weather data in specific locations! 

## License

[MIT](https://choosealicense.com/licenses/mit/)
