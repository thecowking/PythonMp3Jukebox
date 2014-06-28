import pygame.mixer as mixer
import os
from random import shuffle
import socket, threading, fcntl, struct, time
keepAlive = True

class listeners(object):
	"""this is the class for the listeners"""
	def __init__(self, arg):
		super(listeners, self).__init__()
		self.arg = arg

	def music_listener():
		print "End of song watchdog intialised."
		global keepAlive
		while keepAlive:
			if not mixer.music.get_busy():
				data = 'next'
				check_input(data)
				time.sleep(0.1)

	def socket_listener(current_IP, port):
		global keepAlive
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((current_IP, port))
		s.listen(1)
		while keepAlive:
			conn, addr = s.accept()
			data = conn.recv(1024)
			