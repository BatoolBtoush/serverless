from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #request status is successful
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    #where we put the data
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return
