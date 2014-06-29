import pygame.mixer as mixer
import os
from random import shuffle
import socket, process, fcntl, struct, time

class listeners(object):
	"""this is the class for the listeners"""
	def __init__(self, arg):
		super(listeners, self).__init__()
		self.arg = arg

	def music_listener():
		print "End of song watchdog intialised."
			if not mixer.music.get_busy():
				data = 'next'
				check_input(data)
				time.sleep(0.1)

	def socket_listener(self, current_IP, port):
		global keepAlive
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((current_IP, port))
		s.listen(1)
		while keepAlive:
			conn, addr = s.accept()
			data = conn.recv(1024)
			conn.close()
			#send data here

class data_handling(object):
	'''this is the class where I take inputs and deal with them'''
	def __init__(self, arg):
		super(data_handling, self), __init__()
		self.arg = arg

	def command_handler(data):
		if type(data) = str:
			print 'Command recieved'+data
			if data == 'play':
				#insert code to play the current song here.
			elif data == 

class playback(object):