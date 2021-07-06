#!/usr/bin/env python3

import time, os
from ppadb.client import Client

# Default is "127.0.0.1" and 5037
client = Client(host="127.0.0.1", port=5037)

def runner():
    dev_num = 0
    while True:
        devices = client.devices()

        if dev_num != len(devices):
            if len(devices) == 0:
                pass
            else:
                os.system('scrcpy')

        dev_num = len(devices)
        time.sleep(1)

os.system('scrcpy')
runner()
