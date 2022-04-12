from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #parsing the url path’s query string.
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    name = dic.get("name")
    
    if name:
      message = f"Hey {name}"

    else:
      message = "Hey stranger"

    message += f"\nGreetings from Python version {platform.python_version()}"
    
    #request status is successful
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    #showing the image on the screen
    self.path = 'assets/time-pink-floyd.png'
    content = open(self.path, 'rb').read()
    self.wfile.write(content)
    self.wfile.write(message.encode())
    
    return
