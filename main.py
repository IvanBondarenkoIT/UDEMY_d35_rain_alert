import api_manage


def get_api(city_name, country_code):
    api_key = "976e8d42a3ba638fb1d73cea82cdd613"
    # "{'lon': 41.6359, 'lat': 41.6416}" "Batumi"
    params = {
        "lat": 41.6416,
        "lon": 41.6359,
        # "exclude": "",
        "appid": api_key,
    }

    url = "https://api.openweathermap.org/data/2.5/forecast"

    return api_manage.ApiManage(url, params=params).get_json()


if __name__ == '__main__':
    json_data = get_api('Batumi', 'GE')
    will_rain = False
    for hour_data in json_data["list"][:9]:
        condition_code = hour_data['weather'][0]['id']
        if condition_code < 700:
            will_rain = True
            # print(hour_data['dt_txt'], hour_data['weather'][0]['main'])

    if will_rain:
        print("Bring an umbrella.")


