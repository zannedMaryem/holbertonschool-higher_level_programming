#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class CustomHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                # Root path: simple text response
                if self.path == "/" or self.path == "":
                    body = "Hello, this is a simple API!".encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/plain")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return

                # /data: return JSON dataset
                elif self.path == "/data":
                    data = {"name": "John", "age": 30, "city": "New York"}
                    body = json.dumps(data).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return

                # /status: return OK
                elif self.path == "/status":
                    body = "OK".encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/plain")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return

                # Unknown endpoint: 404
                else:
                    msg = "Endpoint not found"
                    body = msg.encode("utf-8")
                    self.send_response(404)
                    self.send_header("Content-Type", "text/plain")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)

httpd = HTTPServer(("localhost", 8000), CustomHandler)
httpd.serve_forever()

