import asyncio
import websockets
import sqlite3
from time import sleep

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            try:
                connection = sqlite3.connect('../webapp/instance/microbit_app.sqlite')
            except:
                print("error")
            c = connection.cursor()
            res = c.execute("SELECT id, status, temp, light FROM microbit WHERE room = ?;", (message,)).fetchall()
            c.close()
            for conn in connected:
                for row in res:
                    toSend = str()
                    for idx, part in enumerate(row):
                        if idx < len(row)-1:
                            toSend += str(part) + ';'
                        else:
                            toSend += str(part)
                    await conn.send(toSend)
                    print(row)
    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()