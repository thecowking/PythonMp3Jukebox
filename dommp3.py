import socket, sys

def get_inputs():
	port = get_port()
	ip= get_ip()

def get_port():
	while True:
		port= raw_input('Please enter listening port number, in the range 20000-30000: ')
		if check_port(port):
			port = int(port)
			get_ip(port)

def get_ip(port):
	while True: 
		ip= raw_input('Please input IPv4 server IP address: ')
		if check_ip(ip):
			wait_for_commands(port, ip)


def check_port(port):
	if len(port)<1:
		print "please input a value"
		return
	else:
		try:
			port = int(port)
		except: 
			print "Port number should be an int"
			return
	if port < 20000 or port > 30000:
		print "Port must be between 20000 and 30000"
		return
	else:
		return True

def check_ip(ip):
	if len(ip)<7:
		print "Invalid IP, please input a valid IPv4 address"
		return
	else:
		return True



def wait_for_commands(port, ip):
	while True:
		command= raw_input('Please input command (play/pause/unpause/stop/next/kill/quit): ')
		if command == 'quit':
			print "bye bye"
			exit(0)
		elif command == "kill":
			print "Closing Server, bye bye"
			send_command(port, ip, 'stop')
			exit(0)
		else:
			send_command(port, ip, command)


def send_command(port, ip, command):
	print command, ip, port
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip,port))
		s.sendall(command)
	except:
		print "Unable to establish connection, please check IP and Port"
		get_inputs()
	
	return 


get_inputs()

#TODO: check for arguments, ie a config file with the information, if that exists, don't get inputs, go straight to the commands



