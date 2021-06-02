import http.server

server_endpoint = ('localhost', 9999)
httpd = http.server.HTTPServer(server_endpoint, http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()