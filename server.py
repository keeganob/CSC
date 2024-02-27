from socket import *

serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

users = {}

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()

        parts = message.split()
        command = parts[0]

        if command == "REGISTER":
            if len(parts) != 3:
                reply = "ERROR invalid registration"
            else:
                username, password = parts[1], parts[2]
                if username in users:
                    reply = "ERROR username exists"
                else:
                    users[username] = password
                    reply = "SUCCESSFUL REGISTRATION"
        elif command == "LOGIN":
            if len(parts) != 3:
                reply = "INVALID CREDENTIALS"
            else:
                username, password = parts[1], parts[2]
                if users.get(username) == password:
                    reply = "SUCCESSFUL LOGIN"
                else:
                    reply = "INVALID CREDENTIALS!"
        else:
            reply = "INVALID COMMAND!"

        print(f"Received info: {message}")
        connectionSocket.send(reply.encode())

        connectionSocket.close()
    except Exception as e:
        print(f"An error occurred: {e}")
