
# -*- coding: utf-8 -*-
import socket
import os

def html_page_maker (data):
    if data == 0:
        return 0
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

def request_manager (client_socket, method, adress, protocol):
    if adress == '/':
        answer = "Hello mister!\r\n"
        answer += "You are: " + "NAME?" + "\r\n" #косяк
        return answer
    request = adress.split('/')
    names = os.listdir("..//files")
    str_names = ' '.join(names)
    if request[1] == "media":
        if len(request) == 2:
            return str_names
        try:
            if len(request) == 3 and names.index(request[2]) != -1:
               file = open("../files/" + request[2], 'r')
               answer = file.read()
               file.close()
               return answer
        except:
            return 0

    if request[1] == "test":
        answer = method + " " + adress + ' ' + protocol
        return answer
    else:
        return 0


def compile_answer(connection, status="200 OK", typ="text/plain; charset=utf-8", data=""): #функция посылает ответ в нужном формате HTTP/1.1
    if data == 0:
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
    decoded_data = decoded_data.split("\r\n", 1)[0]  # берем первую строку запроса
    (method, adress, protocol) = decoded_data.split(" ", 2)  # разделяем строку на 3 по пробелам

    if method != "GET":
        compile_answer(client_socket, "404 Not Found", data="Not GET")
        return

    compile_answer(client_socket, typ="text/html; charset=utf-8",data=html_page_maker(request_manager(client_socket, method, adress, protocol)))

    return 'WRITE YOU RESPONSE HERE\n'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #
server_socket.listen(1)  #

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #
        request_string = client_socket.recv(2048)  #
        client_socket.send(get_response(request_string))  #
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #
        exit()