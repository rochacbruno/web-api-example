import json
from http.server import HTTPServer, BaseHTTPRequestHandler


dados = {"canal": "LinuxTips", "msg": "Vaiiii!"}  # dict


class API(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Ok
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(dados).encode("utf-8"))


server = HTTPServer(("0.0.0.0", 8000), API)
server.serve_forever()
