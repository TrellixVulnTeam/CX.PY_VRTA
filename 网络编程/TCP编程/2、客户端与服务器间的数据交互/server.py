import socket

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定IP和端口
server.bind(('192.168.1.102',8080))

#监听
server.listen(5)
print("服务器启动成功")
#等待连接
clientSocket,clientAddress = server.accept()
print("%s--%s 连接成功" % (str(clientSocket),clientAddress))

while True:
    data = clientSocket.recv(1024)
    print("客户端说：" + data.decode("utf-8"))
    sendData = input("输入给客户端的数据")
    clientSocket.send(sendData.encode("utf-8"))



