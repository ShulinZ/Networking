'''CS6843 Shulin Zhang
'''
import time
import socket

serverHost = ''
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(0,10):
	try:
		seqNum = i
		startTime = time.time()
		startTimep = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
		message = 'Ping seqNum:%d '%seqNum +'startTime:'+ startTimep
		clientSocket.sendto(message,(serverHost,serverPort))
		print 'Send message: \n',message
		clientSocket.settimeout(1)
		recvMessage,addr = clientSocket.recvfrom(1024)
		print 'Response from server:\n',recvMessage
		recvTime = time.time()
		rtt = recvTime - startTime
		print 'RTT:%f '%rtt +' second(s)\n'
	except socket.timeout:
		print 'lost packet (seqNum):%d'%seqNum
clientSocket.close()
