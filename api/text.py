from http.server import BaseHTTPRequestHandler
import time

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #request status is successful
    self.send_response(200)
    self.send_header('Last-Modified', self.date_time_string(time.time()))
    self.end_headers()
    self.wfile.write('Response body\n')
    return
