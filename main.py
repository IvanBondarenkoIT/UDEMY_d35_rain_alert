import api_manage
import config
from send_sms import send_sms


def get_api(lat, lon):
    api_key = "976e8d42a3ba638fb1d73cea82cdd613"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
    }

    url = "https://api.openweathermap.org/data/2.5/forecast"

    return api_manage.ApiManage(url, params=params).get_json()


if __name__ == '__main__':
    json_data = get_api(lat=41.6359, lon=41.6416) # "Batumi"
    will_rain = ''
    for hour_data in json_data['list'][:18]: # срез на 9 для 1 суток, 18 - 2 суток. С пустым значением 5 суток
        condition_code = hour_data['weather'][0]['id']

        if condition_code < 700:
            hd = hour_data['dt_txt'].split(' ')
            will_rain += f"{hd[0][-2:]}:{hd[1][:2]}\n"

    if will_rain:
        print(will_rain)
        send_sms(f"Bring an umbrella.\n{will_rain}", config.my_actual_phone_number)


