import socket
#cli side
ClitcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.179.147"
port = 8000

ClitcpSocket.connect((host, port))

print ClitcpSocket.recv(2048)

while True :
	data_cli = raw_input("> ")
	ClitcpSocket.send(data_cli)
	data_from_srv = ClitcpSocket.recv(2048)
	if data_from_srv == "Bye." :
		ClitcpSocket.close()
		print "> ", data_from_srv
		break
	else :
		print "> ", data_from_srv




