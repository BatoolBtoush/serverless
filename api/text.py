from http.server import BaseHTTPRequestHandler
import time

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #request status is successful
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(time.time().encode()))
    return
