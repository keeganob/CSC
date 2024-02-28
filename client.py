import argparse
from socket import *

parser = argparse.ArgumentParser(description='TCP client for interacting with the server.')
parser.add_argument('--server_ip', type=str, help='IP address of the server', required=True)
parser.add_argument('--server_port', type=int, help='Port number of the server', required=True)
parser.add_argument('--request', type=str, help='Request type (e.g., signup, announce)', required=True)
parser.add_argument('--username', type=str, help='Username for registration or login', required=False)
parser.add_argument('--password', type=str, help='Password for registration or login', required=False)

# Parse the command line arguments
args = parser.parse_args()

serverName = args.server_ip
serverPort = args.server_port
requestType = args.request.lower()
username = args.username
password = args.password

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

if requestType == 'register' and username and password:
    sentence = f"REGISTER {username} {password}"
elif requestType == 'login' and username and password:
    sentence = f"LOGIN {username} {password}"
	
elif requestType == 'list':
	clientSocket.send("LIST".encode())
	user_list = clientSocket.recv(1024).decode()
	sentence = user_list
	print(user_list)

elif requestType == 'chat':
	sentence = 'CHAT'
else:
	sentense = 'UNKNOWN REQUEST TYPE'

clientSocket.send(sentence.encode()) 

modifiedSentence = clientSocket.recv(1024)

print( modifiedSentence.decode())
clientSocket.close()

