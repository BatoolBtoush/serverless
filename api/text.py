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


    first_message = f"\nGreetings from Python version {platform.python_version()}"
    second_message = f"\nGreetings from api/text page"
    #third_message = 


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(first_message.encode())
    self.wfile.write(second_message.encode())

    
    
    return
