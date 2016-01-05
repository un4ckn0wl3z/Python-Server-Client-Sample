#!/usr/bin/python
#Server side....
import socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0"
port = 8000

tcpSocket.bind((host, port))

tcpSocket.listen(2)

print "Server Started...wait for client......"

(client, (ip, port)) = tcpSocket.accept()

print "Recive connection from : ", ip
client.send('Welcome to test server....Type "exit" for exit....\n')



while True :
	data = client.recv(2048)
	print "Recive : ", data

	if data == "exit" :
		client.send("Bye.")
		client.close()
		break
	elif data == "hi" :
		text = "Hi..How r u"
	elif data == "fine" :
		text = "Nice day.."
	elif data == "i love u" :
		text = "Wow... i love u too.."
	else :
		text = data

	client.send(text)
	print "Send : ", text



tcpSocket.close()
print "Server.. close.."
