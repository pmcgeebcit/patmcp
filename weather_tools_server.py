from __future__ import annotations
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-tools")

def _simple_weather_for_city(city: str) -> dict:
    c = city.strip()
    if not c:
        raise ValueError("city must be a non-empty string")

    key = c.lower()
    presets = {
        "vancouver": {"condition": "Rain", "temp_c": 7, "wind_kph": 18},
        "toronto": {"condition": "Cloudy", "temp_c": -2, "wind_kph": 22},
        "calgary": {"condition": "Clear", "temp_c": -10, "wind_kph": 12},
        "montreal": {"condition": "Snow", "temp_c": -6, "wind_kph": 25},
    }
    if key in presets:
        return {"city": c.title(), **presets[key]}

    return {"city": c.title(), "condition": "Sunny", "temp_c": 27, "wind_kph": 2}

@mcp.tool()
def get_weather(city: str) -> dict:
    return _simple_weather_for_city(city)

# FastMCP ASGI app (this is what Uvicorn will serve)
app = mcp.http_app()
