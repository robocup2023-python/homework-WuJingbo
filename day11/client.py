import socket

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        Q = input('输入欲翻译文本：')
        if Q.strip() == '':
            print('欲翻译文本不可以为空！')
            continue
        if len(Q.strip()) > 1000:
            print('欲翻译文本长度不可以超过1000！')
            continue
        client_socket.send(Q.encode())
        response = client_socket.recv(1024).decode()
        print('翻译结果:', response)

    client_socket.close()
