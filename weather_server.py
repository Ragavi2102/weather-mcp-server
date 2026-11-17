
import requests
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Weather MCP Server")


@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather information for a city."""

    # Step 1: Get city coordinates using Geocoding API

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

    except requests.exceptions.RequestException:
        return "Unable to connect to the Geocoding API. Please check your internet connection."

    # Step 2: Check whether the city exists

    if not geo_data.get("results"):
        return f"City not found: {city}"

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 3: Get current weather using Forecast API

    forecast_url = "https://api.open-meteo.com/v1/forecast"

    forecast_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m",
        "timezone": "auto"
    }

    try:
        forecast_response = requests.get(
            forecast_url,
            params=forecast_params,
            timeout=10
        )
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

    except requests.exceptions.RequestException:
        return "Unable to connect to the Forecast API. Please check your internet connection."

    # Step 4: Extract current weather details

    current = forecast_data["current"]

    # Step 5: Return weather information

    return (
        f"City: {city}\n"
        f"Temperature: {current['temperature_2m']} °C\n"
        f"Humidity: {current['relative_humidity_2m']}%\n"
        f"Feels Like: {current['apparent_temperature']} °C\n"
        f"Wind Speed: {current['wind_speed_10m']} km/h"
    )


if __name__ == "__main__":
    mcp.run()
