from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Обработка запроса
        print("requestline: " + self.requestline)
        print("path: " + self.path)
        for key in self.headers.keys():
            print(key)
        print("header User-Agent: " + self.headers.get("User-Agent"))
        print("header Accept: " + self.headers.get("Accept"))
        print("header Accept-Language: " + self.headers.get("Accept-Language"))
        # ответ
        self.send_response(200) # код ответа
        self.send_header("Content-Type", 'text/html') # заголовок ответа
        self.end_headers() # пустая строка
        self.wfile.write(b"<h1>Hello World!</h1>") # тело ответа


address = ('localhost', 3000) # localhost | 127.0.0.1
http = HTTPServer(address, HttpRequestHandler)
http.serve_forever()  # запуск сервера
