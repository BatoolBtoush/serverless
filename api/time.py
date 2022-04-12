from datetime import time
from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
import time


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get("name")

        if name:
            message = f"Hey {name}"

        else:
            message = "Hey stranger"

        message += f"\nGreetings from Python version {platform.python_version()}"
        second_message = f"\nThis is the api/time page"
        third_message = f"\nThis page will show the day, date and time as of today\n"
        time_message = time.localtime(time.time())
        time_message_mod = time.strftime("%A, %m/%d/%Y, %I:%M:%S", time_message)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())
        self.wfile.write(second_message.encode())
        self.wfile.write(third_message.encode())
        self.wfile.write(str(time_message_mod).encode())

        return
