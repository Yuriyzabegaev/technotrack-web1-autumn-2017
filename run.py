# -*- coding: utf-8 -*-
import socket
import os

def html_page_maker (data):
    if data == -1:
        return -1
    answer = """<!DOCTYPE html>"""
    answer += """<html>"""
    answer += """<head>"""
    answer += """<title>HTML Document</title>"""
    answer += """</head>"""
    answer += """<body>"""
    answer += data
    answer += """</body>"""
    answer += """</html>\r\n"""
    return answer

def request_manager (decoded_request, method, adress, protocol):
    if adress == '/':
        n = decoded_request.find("User-Agent: ")
        hello = decoded_request[n+12:]
        answer = "Hello mister!\r\nYour name is " + hello + "\r\n"

        #answer += "You are: " + "NAME?" + "\r\n" #косяк
        return answer
    request = adress.split('/')
    names = os.listdir("../files")
    str_names = ' '.join(names)
    if request[1] == "media":
        if len(request) == 2:
            if request[1] == "media":
                return str_names
        if len(request) == 3:
            if request[1] == "media" and names.index(request[2]) != -1:
                file = open("../files/" + request[2], 'r')
                answer = file.read()
                file.close()
                return answer
            if request[1] == "media" and request[2] == '':
                return str_names

    if request[1] == "test":
        answer = decoded_request
        return answer
    else:
        return -1


def compile_answer(connection, status="200 OK", typ="text/plain; charset=utf-8", data=""): #функция посылает ответ в нужном формате HTTP/1.1
    if data == -1:
        status = "404 Not Found"
        data = "Not GET"
    data = data.decode("utf-8")
    connection.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    connection.send(b"Server: localhost\r\n")
    connection.send(b"Connection: close\r\n")#?
    connection.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    connection.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    connection.send(b"\r\n")  # после пустой строки в HTTP начинаются данные
    connection.send(data)

def get_response(request):
    data = b""
    print "Got new HTTP request\r\n"
    data += request
    if not data:
        return
    decoded_data = data.decode("utf-8")
    decoded_data_1st_str = decoded_data.split("\r\n", 1)[0]  # берем первую строку запроса
    (method, adress, protocol) = decoded_data_1st_str.split(" ", 2)  # разделяем строку на 3 по пробелам

    if method != "GET":
        compile_answer(client_socket, "404 Not Found", data="Not GET")
        return

    compile_answer(client_socket, typ="text/html; charset=utf-8",data=html_page_maker(request_manager(decoded_data, method, adress, protocol)))

    return 'WRITE YOU RESPONSE HERE\n'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #связывает наш сокет с хостом, первый элемент - хост, второй - порт
server_socket.listen(1)  #слушает соединения с сокетом, аргумент - максимальное кол-во подключений в очереди, изменил с 0 на 1

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  # возвращает имя полученного сокета клиента
        request_string = client_socket.recv(2048)  #читаем порциями по 2кб
        client_socket.send(get_response(request_string)) #отправляем результат get_respose
        client_socket.close()
    except KeyboardInterrupt:  #обработка ошибок
        print 'Stopped'
        server_socket.close()  #закрываем сокет
        exit()