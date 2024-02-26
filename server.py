from socket import *
serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to recieve')
while True: 
	try:
		connectionSocket, addr = serverSocket.accept()
		sentence = connectionSocket.recv(1024).decode()
		#sentence recieves the data from the client into the server
	
		print(f"Connection from {addr} has been established")
		print(f"Recieved info: {sentence}") 
		capSentence = sentence.upper()
		connectionSocket.send(capSentence.encode())
		#Sends Message to client 

		connectionSocket.close() 
		#close the connection 
	except Exception as e:
		print(f"an Error occured: {e}")

