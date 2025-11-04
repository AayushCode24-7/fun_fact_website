from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
server_address = ('', PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serving on http://localhost:{PORT}")
httpd.serve_forever()
