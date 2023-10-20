import socket
from threading import Thread
import requests


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        Q = data.decode().strip()
        params = {
            'q': Q,
            'from': 'Auto',
            'to': 'Auto'
        }
        imformation = requests.post(
            'https://aidemo.youdao.com/trans', params)
        json = imformation.json()
        translation = json['translation']
        for x in range(len(translation)):
            client_socket.send(str(translation[x]).encode())

    client_socket.close()


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print('等待客户端连接...')

    while True:
        client_socket, addr = server_socket.accept()
        print('客户端已连接：', addr)

        client_thread = Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

    server_socket.close()
