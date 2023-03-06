import json
from typing import AsyncGenerator

import aiohttp

from src.errors import NotFoundError
from src.weather.models import NWZone, NWForecast


class WeatherClient:
    def __init__(self):
        self._url = "https://api.weather.gov"
        headers = {"User-Agent": "WQ", "Accept": "application/ld+json"}
        self._session = aiohttp.ClientSession(headers=headers, base_url=self._url)

    async def get_zones(self, limit: int = 50) -> AsyncGenerator[NWZone, None]:
        async with self._session.get(f"/zones?limit={limit}") as response:
            txt = await response.text()
            formatted = json.loads(txt)
            for zone in formatted["@graph"]:
                yield NWZone(**zone)

    async def get_forecast(self, zone: NWZone) -> NWForecast:
        async with self._session.get(
            f"/zones/{zone.type}/{zone.id}/forecast"
        ) as response:
            txt = await response.text()
            formatted = json.loads(txt)
            return NWForecast(**formatted)

    async def get_observation(self, zone_id: str):
        async with self._session.get(
                f"/zones/forecast/{zone_id}/observations"
        ) as response:
            if response.status == 404:
                raise NotFoundError
            txt = await response.text()
            formatted = json.loads(txt)
            return NWForecast(**formatted)
