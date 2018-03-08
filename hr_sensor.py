import websocket
import json
import random
import time

ws = websocket.WebSocket()
ws.connect('ws://127.0.0.1:9010/send_patient_data')
try:
    while True:
        data = json.dumps({'hr': random.randrange(90, 110)})
        ws.send(data)
        print('sending {0}'.format(data))
        time.sleep(3)
except Exception:
    ws.close()