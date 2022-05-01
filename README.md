# travel-agency
Provides an API with the data obtained from the weather API. Our API should provide the functionality to see the current weather for a given location (receiving a latitude and longitude for it), the weather forecast(avg. temperature and condition like sunny, cloudy, etc) for the next five days for a given location.

## Installation on Mac
1. `git clone` the repository
2. python must be installed, can be checked by `python3 --version`
3. install pip `sudo easy_install pip`
4. install a virtual environment then activate it
    ```
    pip install virtualenv
    python3 -m venv venv
    . venv/bin/activate
    ```
5. install the dependencies `pip install -r requirements.txt`
6. go to `travel-agency` folder and create an `.env` file with API_KEY (your openweathermap api key)
7. make migrations then migrate
    ```
   ./manage.py makemigrations
   ./manage.py migrate
   ```
8. run `./manage.py create_cities` and `./manage.py create_init_destination_types`. this will create all capitals and few destination types.
9. run `./manage.py runserver`
