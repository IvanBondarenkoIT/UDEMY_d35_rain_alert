import api_manage


def get_api(city_name, country_code):
    api_key = "976e8d42a3ba638fb1d73cea82cdd613"
    params = {
        "q": f"{city_name},{country_code}",
        "appid": api_key,
    }

    return api_manage.ApiManage("https://api.openweathermap.org/data/2.5/weather", params=params).get_json()


if __name__ == '__main__':
    print(get_api("Batumi", "GE"))

    # "{'lon': 41.6359, 'lat': 41.6416}"

