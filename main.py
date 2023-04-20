import api_manage


def get_api(city_name, country_code):
    api_key = "976e8d42a3ba638fb1d73cea82cdd613"
    params = {
        "q": f"{city_name},{country_code}",
        "appid": api_key,
    }

    params_one_call = {
        "lat": 41.6416,
        "lon": 41.6359,
        # "exclude": "",
        "appid": api_key,
    }

    # api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

    # ?lat = {lat} & lon = {lon} & exclude = {part} & appid = {API key}

    url = "https://api.openweathermap.org/data/2.5/weather"
    url_one_call = "https://api.openweathermap.org/data/2.5/forecast"

    return api_manage.ApiManage(url_one_call, params=params_one_call).get_json()


if __name__ == '__main__':
    print(get_api("Batumi", "GE"))

    # "{'lon': 41.6359, 'lat': 41.6416}"

