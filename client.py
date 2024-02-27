import argparse
from socket import *

parser = argparse.ArgumentParser(description='TCP client for interacting with the server.')
parser.add_argument('--server_ip', type=str, help='IP address of the server', required=True)
parser.add_argument('--server_port', type=int, help='Port number of the server', required=True)
parser.add_argument('--request', type=str, help='Request type (e.g., signup, announce)', required=True)

# Parse the command line arguments
args = parser.parse_args()

serverName = args.server_ip
serverPort = args.server_port
requestType = args.request

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

if requestType == 'Register':
	sentence = 'REGISTER!'	
	
elif requestType == 'List':
	sentence = 'LIST!'

elif requestType == 'Chat':
	sentence = 'CHAT'
else:
	sentense = 'UNKNOWN REQUEST TYPE'

sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode()) 

modifiedSentence = clientSocket.recv(1024)

print('From Server:', modifiedSentence.decode())
clientSocket.close()

