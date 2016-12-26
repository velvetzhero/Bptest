#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8090

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        global counter
        self.send_response(200)
        self.send_header('Content-type','text/html')
        #Will raise the count for every GET request received
        if "GET" in self.command:
            print self.command
            counter = counter + 1
            print counter
        self.end_headers()
        # Send the html message
        self.wfile.write(counter)
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    counter=0
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming  requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
