#!/usr/bin/env python3

import asyncio
import websockets
import json

port = 8765
print("WebSocket Server listening on port " + str(port))

async def hello(websocket, path):
    json_data = await websocket.recv()
    print("")
    print("JSON file received:")
    print("------------------------------")
    print(json.dumps(json.loads(json_data), indent=2, sort_keys=True))


start_server = websockets.serve(hello, 'localhost', port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



