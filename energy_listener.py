import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.12',25001))
s.listen(1)
while True:
	conn, addr = s.accept()
	data = conn.recv(20480)
	conn.close()
	print data 