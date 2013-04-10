'''
Shulin Zhang 0494786 NYU-poly CS6843
'''
import socket
import ssl
import time
import pprint
import base64

msg="\r\n I love networking \r\n"
endmsg="\r\n.\r\n"

# choose a mail server (e.g. a Google server) and call it mailserver
#mailserver = ("smtp.gmail.com", 587)
mailserver = ("smtp.gmail.com", 465)

# create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_clientSock = ssl.wrap_socket(clientSocket)

ssl_clientSock.connect(mailserver)

recv=ssl_clientSock.recv(10240)


print "reply for connection : " + recv
if recv[:3]!='220':
	print ('220 reply not received from server connection.')
 
#Send HELO command and print server response.

heloCommand='HELO Alice\r\n'
ssl_clientSock.send(heloCommand)
recv1 = ssl_clientSock.recv(10240)

print '/////////////'
print 'reply for HELO ' + recv1
if recv1[:3]!='250':
	print ('250 reply not received from server helo.')



'''

#Send MAIL FROM command and print server response.
#Fill in start
mailCommand = 'STARTTLS\r\n'
ssl_clientSock.send(mailCommand)
print "send startls"
recvMail = ssl_clientSock.recv(1024)
print '/////////////'
print recvMail #should be 220 go ahead
'''


#login
certificate_der = ssl_clientSock.getpeercert(True)
ssl_clientSock.send('AUTH LOGIN\r\n')
recv_login = ssl_clientSock.recv(1024)
print '///////////////'
print "auth login reply " + recv_login

print '///////////////'
ssl_clientSock.send(base64.b64encode('shulinzhang0225@gmail.com')+'\r\n')
recv_username = ssl_clientSock.recv(1024)
print "username reply " + recv_username

print '///////////////'
ssl_clientSock.send(base64.b64encode('password')+'\r\n')
recv_pwd = ssl_clientSock.recv(1024)
print "pwd reply " + recv_pwd #should be accept


mailfromCommand = 'MAIL FROM:<shulinzhang0225@gmail.com>\r\n'
ssl_clientSock.send(mailfromCommand)
print ('Sending MAIL FROM command to mailserver...')
recv2 = ssl_clientSock.recv(1024)
print recv2
if recv2[:3]!='250':
	print ('250 reply not received from server mailfrom')
#Fill in end
 
#Send RCPT TO command and print server response.
#Fill in start

rcpttoCommand = 'RCPT TO:<shulinzhang0225@gmail.com>\r\n'
ssl_clientSock.send(rcpttoCommand)
print ('Sending RCPT TO command to mailserver...')
recv3 = ssl_clientSock.recv(1024)
print recv3
if recv3[:3]!='250':
	print ('250 reply not received from server rcpt to')
 
#Fill in end
 
#Send DATA command and print server response.
#Fill in start

dataCommand = 'DATA\r\n'
ssl_clientSock.send(dataCommand)
print ('Sending DATA command to mailserver...')
recv4 = ssl_clientSock.recv(1024)
print recv4
if recv4[:3]!='354':
	print ('354 reply not received from server data')
#Fill in end
 

#message ends with a single period.
#Fill in start
ssl_clientSock.send('From: "shulinzhang" <shulinzhang0225@gmail.com>\r\n')
ssl_clientSock.send('To: "shulinzhang" <shulinzhang0225@gmail.com>\r\n')
#send message data.
#Fill in start
ssl_clientSock.send(msg)
#sent_msg = ssl_clientSock.recv(1024)
#print(sent_msg)
#Fill in end
 
ssl_clientSock.send(endmsg)
sent_endmsg = ssl_clientSock.recv(1024)
print(sent_endmsg)
#Fill in end
 
#send QUIT command and get server response.
#Fill in start

quitCommand = 'QUIT\r\n'
ssl_clientSock.send(quitCommand)
print ('Sending QUIT command to mailserver...')
recv5 = ssl_clientSock.recv(1024)
print recv5
if recv5[:3]!= '221':
	print('221 reply not received from server quit')
#Fill in end



