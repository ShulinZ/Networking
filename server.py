'''
Shulin Zhang NYU-poly CS6843
'''
#import socket module
import socket
HOST = ''
PORT = 1234
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
while True:
#enstablish the connection
        print ('Ready to server...')
        connectionSocket, addr = serverSocket.accept()
        print ('Connected by:', addr)
        try:
                message = connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.readlines()
                f.close()
                #send one http header line to socket
                response = 'HTTP/1.1 200 OK\r\n\r\n'
                connectionSocket.send(response.encode())
                #send the content of the request file to client
                for i in range(0,len(outputdata)):
                        connectionSocket.send(outputdata[i].encode())
                print('GOT THE PAGE: ', filename)
                connectionSocket.close()
        except IOError:
                #Send response message for file not found
                notfindMessage = 'HTTP/1.1 404 Not Found\r\n\r\n'
                connectionSocket.send(notfindMessage.encode())
                print ('404 NOT FOUND THE PAGE')
                outputdata = '404 Not Found'
                for i in range(0,len(outputdata)):
                        connectionSocket.send(outputdata[i].encode())
                #Close client socket
                connectionSocket.close()
serverSocket.close()
