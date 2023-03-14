import os
import socket
import time
import threading

def ecouter ():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]

if not os.path.isdir('sharing'):
	os.system('mkdir sharing')


def gestion_client(sock,adress):
	while True:
		msg = sock.recv(2*1024).decode('utf-8')
		msg = msg.split('@')
		file_name = msg[0]
		file_size = msg[1]
		ars       = msg[2] 

		
		if not file_name =='lio':
			
			with open("./sharing/" + file_name, "wb") as file:
				c = 0
	# Starting the time capture.
				start_time = time.time()

	# Running the loop while file is recieved.
				while c <= int(file_size):
					data = sock.recv(1024)
					if not (data):
						break
					file.write(data)
					c += len(data)

	# Ending the time capture.
				end_time = time.time()
    
		
		
		
		
		if ars == "true":
		

			break
	sock.close()











server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = ecouter()
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)





while True:
	server_socket.listen(5)
	con , adres= server_socket.accept()

	
	
	www= threading.Thread(target=gestion_client,args=(con,adres))
	www.start()