from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    name = dic.get("name")

    if name:
        message = f"image of {name}"

    else:
        message = "image of Pink Floyd - Time"

    message = f"\nGreetings from Python version {platform.python_version()}"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.path = 'assets/time-pink-floyd.png'
    content = open(self.path, 'rb').read()
    self.wfile.write(message)
    self.wfile.write(content)
    
    
    return
