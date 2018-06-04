import socket

#TCP通信
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1',50007))
    s.sendall(b'Hello')
    data=s.recv(1024)
    print(repr(data))

#UDP通信
# with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
#     s.sendto(b'Hello UDP',('127.0.0.1',50007))
