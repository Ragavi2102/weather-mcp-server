# Weather MCP Server and Client

A Python-based Weather MCP project that allows an MCP client to retrieve current weather information for a given city using the Open-Meteo APIs.

## Project Overview

This project demonstrates how to build a Model Context Protocol (MCP) server and connect it to an MCP client using Python.

The server exposes a tool called `get_weather`, which accepts a city name, retrieves its geographical coordinates, and fetches its current weather information.

## Features

- Retrieve current weather information by city name.
- Convert city names into geographical coordinates using the Open-Meteo Geocoding API.
- Fetch current weather details using the Open-Meteo Forecast API.
- Expose weather functionality through an MCP tool.
- Connect the MCP client and server using STDIO transport.
- Handle invalid city names and API connection errors.

## Technologies Used

- Python
- MCP Python SDK
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Forecast API
- uv

## Project Structure

```text
mcp-learning/
│
├── weather_server.py
├── client.py
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## How It Works

1. The MCP client starts the weather server as a subprocess.
2. The client connects to the server using STDIO.
3. The client discovers the available MCP tools.
4. The user enters a city name.
5. The client calls the `get_weather` tool.
6. The server uses the Geocoding API to find the city's latitude and longitude.
7. The server calls the Forecast API to retrieve current weather information.
8. The server returns the weather details to the client.

## Weather Information Retrieved

- Temperature (°C)
- Relative Humidity (%)
- Feels-like Temperature (°C)
- Wind Speed (km/h)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ragavi2102/weather-mcp-server.git
```

### 2. Navigate to the project directory

```bash
cd weather-mcp-server
```

### 3. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if it is not already installed.

Then run:

```bash
uv sync
```

### 4. Run the MCP client

```bash
uv run python client.py
```

Enter a city name when prompted to retrieve its current weather information.

The client automatically launches the MCP server.

## APIs Used

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo Forecast API](https://open-meteo.com/en/docs)

No API key is required for the Open-Meteo APIs used in this project.

## Learning Outcomes

- Understanding MCP architecture: Host, Client, and Server.
- Creating MCP tools using Python.
- Understanding tool discovery and tool execution.
- Connecting an MCP client to a server using STDIO.
- Integrating external REST APIs into an MCP server.

## Author

**Ragavi S**

GitHub: [Ragavi2102](https://github.com/Ragavi2102)
