'''CS6843 Shulin Zhang 0494786
'''
import socket
import random
 
#create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
	print 'Ready to server...'
	#generate random number in the range of 10
	message, address = serverSocket.recvfrom(1024)
	rand = random.randint(0,10)
	message = message.upper()
	print message + ' rand number:%d'%rand
	#if "rand" is less is than 4, we consider the packet lost and do not respond
	if rand < 4:
		continue
		#otherwise, the server responds
	serverSocket.sendto(message, address)
	
