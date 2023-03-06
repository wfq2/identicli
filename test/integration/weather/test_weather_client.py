import pytest

from src.errors import NotFoundError
from src.weather.weather_client import WeatherClient
from src.weather.models import NWZone


@pytest.fixture
def weather_client():
    return WeatherClient()


@pytest.mark.asyncio
async def test_get_zones(weather_client):
    async for zone in weather_client.get_zones():
        assert isinstance(zone, NWZone)


@pytest.mark.asyncio
async def test_get_forecast(weather_client):
    zone = None
    async for z in weather_client.get_zones(1):
        zone = z
    forecast = await weather_client.get_forecast(zone)
    print(forecast)


@pytest.mark.asyncio
async def test_get_observation(weather_client):
    async for zone in weather_client.get_zones(50):
        try:
            forecast = await weather_client.get_observation(zone.id)
            print(forecast)
        except NotFoundError:
            continue
