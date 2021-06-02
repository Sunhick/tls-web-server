import http.server
import sys

def main(args):
    server_endpoint = ('localhost', 9999)
    httpd = http.server.HTTPServer(server_endpoint, http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main(sys.argv)