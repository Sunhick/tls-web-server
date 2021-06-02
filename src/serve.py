import http.server
import sys
import ssl

def main(args):
    server_endpoint = ('localhost', 9999)
    httpd = http.server.HTTPServer(server_endpoint, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                server_side=True,
                                certfile='./certs/localhost.crt',
                                keyfile='./certs/localhost.key')
    httpd.serve_forever()

if __name__ == '__main__':
    main(sys.argv)