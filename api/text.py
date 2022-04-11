from datetime import datetime, time
from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
import time


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components =parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)


    first_message = f"\nGreetings from Python version {platform.python_version()}"
    second_message = f"\nGreetings from api/time page"
    third_message = f"\nThis page will show the time"
    time_message = time.time()


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(first_message.encode())
    self.wfile.write(second_message.encode())

    self.wfile.write(str(time_message).encode())

    
    
    return
