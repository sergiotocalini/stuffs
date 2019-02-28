#!/usr/bin/env python3
from ibapi.common import EClient as ibConnection
con = ibConnection(port=7496,clientId=1)
print(con.connect())
