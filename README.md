# Simple Python Websocket Server-Client Example

A very simple WebSocket Server-Client example. The WebSocket server listens on port 8765 and print json files sent by the client.

## Requierements:

To run this example, you need:
 
- Python 3.6 or higher.

- [WebSockets for Python 3] (http://websockets.readthedocs.io/). To install this library:

	```$ pip3 install websockets```

 
## Running

The WebSocket server listens on port 8765 and print json files sent by the client. To run the server on the terminal:

```$ python3 server.py```

You can test that the server is working by running the client example:

```$ python3 client.py```
