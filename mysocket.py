import socket
import sys
try:
	print("creating socket..")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("socket created..")
except socket.error as err:
	print("socket creation failed with error %s" %(err))
port = 80
try:
	host_name = "www.google.com"
	ip = socket.gethostbyname(host_name)
	print(ip)
except socket.gaierror:
	print("there was an error resolving host")
	sys.exit()

# connecting to server on port 80
s.connect((ip,port))
print("socket has been successfully created for the host : "+host_name+ "on port :",port)