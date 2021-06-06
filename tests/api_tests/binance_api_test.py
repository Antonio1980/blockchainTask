from config_definition import BaseConfig
import asyncio
import websockets


async def main():
    uri = BaseConfig.BINANCE_API_URL.format("btcusdt")
    async with websockets.connect(uri) as client:
        print(await client.recv())
        # print(client.send("just_string_bytes".encode("utf-8")))


if __name__ == "__main__":
    # print(BaseConfig.BINANCE_API_URL.format("btcusdt"))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
