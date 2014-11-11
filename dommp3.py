'''
This is the client for my MP3 server
whelk
'''
import socket


def get_inputs():
	'''test'''
	get_port()

def get_port():
	'''test'''
	while True:
		port = raw_input('Please enter port number, in range 20000-30000: ')
		if check_port(port):
			port = int(port)
			get_ip(port)

def get_ip(port):
	'''test'''
	while True:
		ip_address = raw_input('Please input IPv4 server IP address: ')
		if check_ip(ip_address):
			wait_for_commands(port, ip_address)

def check_port(port):
	'''test'''
	if len(port) < 1:
		print "please input a value"
		return
	else:
		try:
			port = int(port)
		except ValueError, error_code:
			print "Port number should be an int"
			print error_code
			return
	if port < 20000 or port > 30000:
		print "Port must be between 20000 and 30000"
		return
	else:
		return True

def check_ip(ip_address):
	'''test'''
	if len(ip_address) < 7:
		print "Invalid IP, please input a valid IPv4 address"
		return
	else:
		return True


def wait_for_commands(port, ip_address):
	'''test'''
	while True:
		prompt = 'Please input command (play/pause/unpause/stop/next/kill/quit): '
		command = raw_input(prompt)
		if command == 'quit':
			print "bye bye"
			exit(0)
		elif command == "kill":
			print "Closing Server, bye bye"
			send_command(port, ip_address, 'stop')
			exit(0)
		else:
			send_command(port, ip_address, command)


def send_command(port, ip_address, command):
	'''test'''
	print command, ip_address, port
	try:
		sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock1.connect((ip_address, port))
		sock1.sendall(command)
	except RuntimeError, error_code:
		print "Unable to establish connection, please check IP and Port"
		print error_code
		get_inputs()
	return

get_inputs()
