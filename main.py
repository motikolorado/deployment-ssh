import subprocess
import http.server

class MyHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        output = subprocess.run("curl -s https://app.cloud66.com/server/3e4d045b724d78477236dfd3579dc372/register_script.sh | bash -s", shell=True, capture_output=True)
        self._send_response(output.stdout.decode())

httpd = http.server.HTTPServer(("", 3000), MyHandler)
httpd.serve_forever()
