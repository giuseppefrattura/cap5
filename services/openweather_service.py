from typing import Optional
import requests
import httpx

from infrastucture import weather_cache
from model.validation_error import ValidationError

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    print(url)

    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    return data


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:

    if forecast:= weather_cache.get_weather(city, state, country, units):
        return forecast

    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    print(url)

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, resp.status_code)
        # resp.raise_for_status()

    data = resp.json()
    forecast = data['main']

    weather_cache.set_weather(city, state, country, units, forecast)

    return forecast
