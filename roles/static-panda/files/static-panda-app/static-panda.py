#!/usr/bin/env python
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os

# Changing doc. root to resources
os.chdir('resources')

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer

# Binding to any ip
server_address = ("0.0.0.0", 8080)
Handler.protocol_version = 'HTTP/1.0'
# Raising a server, which handler's will look for index.html inside the doc. root folder
server = Server(server_address,Handler)
print 'Started static-panda httpserver'
try:
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
