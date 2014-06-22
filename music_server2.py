import os, sys, pygame, random, socket, threading, fcntl, struct, time
keepAlive = True
pygame.mixer.init()
endofsong = 3141
song = 0

def scan_subdirectories(directory):
	mp3list = []
	songlist =[]
	songdict= {}
	for dirpath, subdirs, files in os.walk(directory):
		for x in files:
			if x.endswith('.mp3'):
				mp3list.append(os.path.join(dirpath, x))
				songlist.append(x)
	for song in range(len(songlist)):
		songdict[mp3list[song]]= songlist[song]	
	#print mp3list, songlist, songdict

	return mp3list,songlist, songdict

def scan_single_dir(directory):
	mp3list = []
	songlist =[]
	songdict = {}
	for files in  os.listdir(directory):
		if files.endswith('.mp3'):
				mp3list.append(os.path.join(directory, files))
				songlist.append(files)
	for song in range(len(songlist)):
		songdict[mp3list[song]]= songlist[song]
	return mp3list, songlist, songdict

def randomise_playlist(mp3list):
	random.shuffle(mp3list)
	return mp3list

def play_playlist(mp3list, songdict):
	print "Starting music playback"
	song = check_input(mp3list, songdict, 'play')
	
def play_current_song(mp3list, songdict, song):
	pygame.mixer.music.load(mp3list[song])
	pygame.mixer.music.set_endevent(endofsong)
	pygame.mixer.music.play(0,0.1)
	songpath = mp3list[song]
	songname = songdict[songpath]
	print "Now playing "+songname
	return song
	
def check_for_playlist(song, mp3list):
	if song == len(mp3list):
	  	print "End of playlist"
	  	exit(0)
	else:
		return

def check_input(mp3list ,songdict, data ):
	print 'Command received: ' + data
	if type(data) is str:
		global keepAlive
		global song
		if data == 'play':
			song = play_current_song(mp3list, songdict, song)
			return song
		elif data == 'pause':
			pygame.mixer.music.pause()
			return song
		elif data == 'unpause':
			pygame.mixer.music.unpause()
			return song
		elif data == 'stop':
			pygame.mixer.music.stop()
			keepAlive = False
			print "Ending program"
			exit(0)
		elif data == 'next':
			song = song + 1
			check_for_playlist(song, mp3list)
			song = play_current_song(mp3list, songdict, song)
			return song
		else: 
			print "unrecognised string, please try again, options are play/pause/unpause/stop/next/kill/quit"
			return song

def socket_listener(current_IP, x):
	global keepAlive
	global song
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((current_IP,x))
	s.listen(1)
	while keepAlive:
		conn, addr = s.accept()
		data = conn.recv(1024)
		conn.close()
		data_handler(song ,data)


def data_handler(song, data):
	song = check_input(mp3list ,songdict, data)
	return song

def process_event(event):
	if event.type == endofsong:
		song = check_input('next', songdict, mp3list, song)
	else: 
		return event
		

def ears (mp3list, songdict):
	global keepAlive
	global song
	while keepAlive:
		if not pygame.mixer.music.get_busy():
				song = check_input('next', songdict, mp3list)
				time.sleep(.1)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def open_socket(current_IP):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	for x in range(20000,30000):
		try:
			s.bind((current_IP, x))
			return x	
		except:
			pass


current_IP = get_ip_address('eth0')
current_IP = str(current_IP)
x = open_socket(current_IP)
print 'listening on '+current_IP+":"+str(x)



#start up a thread to listen on an open socket for commands
l= threading.Thread(target= socket_listener, args=(current_IP, x))
l.start()

if len(sys.argv) <1:
	print "Please input the following arguments: absolute path to directory to be played,\n i.e. /home/user/Music\n play subdirectories(yes, no, default no)\n i.e. yes\n shuffle on(yes,no, default no)\n i.e. yes"
directory = sys.argv[1]
if sys.argv[2] == 'yes':
	(mp3list, songlist, songdict)= scan_subdirectories(directory)
elif sys.argv[2] == 'no':
	print "Hello!"
	(mp3list, songlist, songdict)= scan_single_dir(directory)
else:
	print "I assume you meant yes since you didn't say no"
	(mp3list, songlist, songdict)=scan_subdirectories(directory)
if sys.argv[3] == 'yes':
	mp3list = randomise_playlist(mp3list)
#start up a thread to check when the song finishes and increment the counter
t = threading.Thread(target=ears, args= (songdict, mp3list))
t.start()
play_playlist(mp3list, songdict)