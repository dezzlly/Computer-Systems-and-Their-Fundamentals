import socket
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime

HOST, PORT = '', 3000
SOCKET_HOST, SOCKET_PORT = 'socket_server', 5000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self._serve_file('templates/index.html')
        elif self.path == '/message':
            self._serve_file('templates/message.html')
        elif self.path.startswith('/static/'):
            self._serve_file(self.path.lstrip('/'), content_type=self._guess_type(self.path))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/message':
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length)
            data = parse_qs(post_data.decode())

            message = {
                "username": data.get("username", [""])[0],
                "message": data.get("message", [""])[0],
                "date": datetime.now().isoformat()
            }

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SOCKET_HOST, SOCKET_PORT))
                s.send(str(message).encode())

            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_error(404)

    def _serve_file(self, filename, content_type='text/html'):
        try:
            with open(filename, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self._serve_file('templates/error.html')

    def _guess_type(self, path):
        if path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.png'):
            return 'image/png'
        return 'application/octet-stream'


if __name__ == '__main__':
    httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"HTTP server running at http://localhost:{PORT}")
    httpd.serve_forever()
