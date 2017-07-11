#!/usr/bin/env python

import asyncio
import websockets
import json

json_data = json.dumps(['test', {'websocket': ('workshop', None, 1.0, 2)}])

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(json_data)

asyncio.get_event_loop().run_until_complete(hello())

