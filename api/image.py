from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #request status is successful
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.path = 'assets/time-pink-floyd.png'
    content = open(self.path, 'rb').read()
    self.wfile.write(content)
    
    return
