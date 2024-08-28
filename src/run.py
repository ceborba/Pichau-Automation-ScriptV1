import asyncio
from websockets.server import serve
import checkout as checkout

running = False
checkout = checkout.Checkout()

def reset_running():
    global running
    running = False

async def echo(websocket):
    global running, checkout
    async for message in websocket:
        print("Link encontrado: " + message)
        if running is False:
            checkout.start(message, reset_running)
            running = True 
        else:
            print("Selenium already running")

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
