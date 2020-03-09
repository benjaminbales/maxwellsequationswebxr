import BaseHTTPServer, SimpleHTTPServer
import ssl
 
## Variables you can modify
 
#openssl req -x509 -newkey rsa:4096 -keyout server1.example.com.key -out server1.example.com.pem -days 365 -nodes

bind_to_address = ''
server_port = 8080
ssl_key_file = "/Users/benjaminbales/Documents/GoTeachMe/ProductDev/WebXR/server1.example.com.key"
ssl_certificate_file = "/Users/benjaminbales/Documents/GoTeachMe/ProductDev/WebXR/server1.example.com.pem"
 
 
## Don't modify anything below
 
httpd = BaseHTTPServer.HTTPServer((bind_to_address, server_port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,
                                keyfile=ssl_key_file,
                                certfile=ssl_certificate_file)
httpd.serve_forever()
