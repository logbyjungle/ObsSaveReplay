
from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os
from typing import cast

host = "localhost"
port = 4455
load_dotenv()
password = cast(str,os.getenv("password"))

ws = obsws(host, port, password)
ws.connect()
ws.call(requests.SaveReplayBuffer())
ws.disconnect()
