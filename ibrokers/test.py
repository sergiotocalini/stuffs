#!/usr/bin/env python3
import os
import struct
import signal
import socket

import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class TWS(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def connectAck(self):
        print('Connected')


signal.signal(signal.SIGINT, signal.SIG_DFL)
try:                                        
    tws = TWS()
    tws.connect('ibgw.prod.amana.vpn', 4002, clientId=1)
    tws.conn.socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
    tws.run()
except KeyboardInterrupt:
    tws.conn.socket.close()
    os._exit(0)
