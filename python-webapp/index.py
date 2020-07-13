import  time,os
from http.server import *
from io import BytesIO
from os import curdir, sep

HOST_NAME = ""
PORT=8000

sth = """
<html>
    <head>
        <title>Python is awesome!</title>
    </head>
    <body>
        <h1>Afternerd</h1>
        <p>Congratulations! The HTTP Server is working!</p>
    </body>
</html>
"""

REDIRECTIONS = {"/": "/index.html"}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def run():
        httpd = HTTPServer((HOST_NAME,PORT),SimpleHTTPRequestHandler)
        print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME,PORT))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print(time.asctime(),'Stop Server - %s:%s' %(HOST_NAME,PORT))
        
    def send_redirect(self , page="index.html"):
        self.send_response(301)        
        self.send_header("Location", page)
        self.end_headers()
    def load_binary(file):
        with open(file, 'rb') as file:
            return file.read()
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                f = open(curdir + sep + self.path, 'r', encoding="utf-8")
                send = f.read().encode()
                f.close()

                sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                f = open(curdir + sep + self.path, 'rb')
                send = f.read()
                f.close()
                sendReply = True

            if self.path.endswith(".gif"):
                mimetype='image/gif'
                f = open(curdir + sep + self.path, 'rb')
                send = f.read()
                f.close()
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                f = open(curdir + sep + self.path, 'r', encoding="utf-8")
                send = f.read().encode()
                f.close()
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                f = open(curdir + sep + self.path, 'r', encoding="utf-8")
                send = f.read().encode()
                f.close()
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(send)

        except Exception as e:
            f = str(e)
            self.send_error(404,f)
            

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
    
    def do_PUT(self):
        send_redirect(self)
		
    def do_PATCH(self):
        send_redirect(self)
		
    def do_DELETE(self):
        send_redirect(self)
		
    def do_COPY(self):
        send_redirect(self)
        
    def do_HEAD(self):
        send_redirect(self)
		
    def do_OPTIONS(self):
        send_redirect(self)
		
    def do_LINK(self):
        send_redirect(self)
		
    def do_UNLINK(self):
        self.send_response(501)
        self.end_headers()
		
    def do_PURGE(self):
        send_redirect(self)
		
    def do_LOCK(self):
        send_redirect(self)
		
    def do_UNLOCK(self):
        send_redirect(self)
		
    def do_PROFIND(self):
        send_redirect(self)
		
    def do_VIEW(self):
        send_redirect(self)
        
    
        
if __name__ == "__main__":
    SimpleHTTPRequestHandler.run()

