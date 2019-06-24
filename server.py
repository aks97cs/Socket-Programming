import socket

# creating socket object
s = socket.socket()
print("socket has been successfully created")
port = 12345
# binding port for listening
s.bind(('',port))
print("socket binded to the port",port)

# putting server on listening mode
s.listen(5)
print("socket is ready to listen")

while True:
	# establish connection with client
	c, addr = s.accept()
	print("Got connection form ",addr)
	c.send("Thank you for connecting")
	c.close()