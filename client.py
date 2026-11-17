from mcp import Client, StdioServerParameters
import asyncio
import sys

server_params = StdioServerParameters(
    command=sys.executable,
    args=["weather_server.py"]
)

async def main():
    async with Client(server_params) as client:
        print("Connected to Weather MCP Server")

        tools = await client.list_tools()
        print("Available tools:", [tool.name for tool in tools.tools])

        city = input("Enter city name: ")

        result = await client.call_tool(
            "get_weather",
            {"city": city}
)
        

        print("Weather:", result.structured_content["result"])

if __name__ == "__main__":
    asyncio.run(main())