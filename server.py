from socket import *

serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen(1)
print('The server is ready to recieve')

users = {} 

while True: 
	try:
		connectionSocket, addr = serverSocket.accept()
		sentence = connectionSocket.recv(1024).decode()
		#sentence recieves the data from the client into the server
		
		command, *data = sentence.split()

		if command == "REGISTER":
			if len(data) != 2:
				reply = "ERROR invalid registration"
			else:
				username, password = data
				if username in users:
					reply = "ERROR username exists"
					
				else:
					users[username] = password
					reply = "SUCCESSFUL REGISTRATION"
		elif command == "LOGIN"
			if len(data) != 2:
				reply = "INVALID CREDENTIALS"
			else:
				username, password = data
				
				if username in users and users[username] == password:
					reply = "SUCCESSFULL LOGIN"
				else:
					reply = "INVALID CREDENTIALS!"

		else:
			reply = "INVALID COMMAND!"
                  
				
		print(f"Recieved info: {sentence}") 
		capSentence = sentence.upper()
		connectionSocket.send(reply.encode())
		#Sends Message to client 

		connectionSocket.close() 
		#close the connection 
	except Exception as e:
		print(f"an Error occured: {e}")

