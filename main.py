from wrapper import Wrapper
import asyncio
import time
from websockets.server import serve
import json

mywrapper = Wrapper()

def current_milli_time():
    return round(time.time() * 1000)

async def echo(websocket):
    async for message in websocket:
        message = json.loads(message)
        func = getattr(mywrapper, message['type'])
        func(*message['params'])
        

async def main():
    async with serve(echo, "localhost", 61565):
        await asyncio.Future()  # run forever

asyncio.run(main())