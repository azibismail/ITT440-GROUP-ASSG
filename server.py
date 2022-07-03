import socket
import os
import sys
import json
import random
import errno
import math
from multiprocessing import Process

def process_start(s_sock):

	s_sock.send(str.encode("*****ASA BOOKSTORE*****"))
	
	while True:
		data = s_sock.recv(2048)
		data = data.decode("utf-8")
		
		try:
			menu, num, value = data.split(":")
			opt = str(menu)
			qty = int(num)
			prc = float(value)
			
			if opt[0] == 'A':
				opt = 'Bisik Ombak Gelora'
				prc = 35.90
				ans = qty * (prc)
				
			elif opt[0] == 'B':
				opt = 'Nasi Lemak Untuk Emak'
				prc = 30
				ans = qty * (prc)
				
			elif opt[0] == 'C':
				opt = 'Mathematics for Dummies'
				prc = 55
				ans = qty * (prc)
				
			elif opt[0] == 'D':
				opt = 'English for Dummies'
				prc = 40
				ans = qty * (prc)
				
			elif opt[0] == 'E':
				opt = 'Kau Yang Terindah'
				prc = 30.90
				ans = qty * (prc)
				
			elif opt[0] == 'F':
				opt = 'Hanya Kita Sahaja'
				prc = 35.50
				ans = qty * (prc)
				
			elif opt[0] == 'G':
				opt = 'Firdaus Untuk Melur'
				prc = 4.99
				ans = qty * (prc)
				
			elif opt[0] == 'H':
				opt = 'Hanya Melur'
				prc = 99.99
				ans = qty * (prc)
				
			elif opt[0] == 'I':
				opt = 'Jangan Baca Buku Ini'
				prc = 41.90
				ans = qty * (prc)
				
			elif opt[0] == 'J':
				opt = 'Cubaan 1..2..3!'
				prc = 25.50
				ans = qty * (prc)
				
			else:
				answer = ('ERROR')
				
			sendtoCli = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
			print(sendtoCli)
			print('ORDER RECEIVED!!!!')
			
		except:
			print('Connection Terminated')
			sendtoCli = ('Connection Terminated')
			break
			
		if not data:
			break
			
		s_sock.send(str.encode(str(sendtoCli)))
	s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("",8888))
	print("Waiting for client connection...")
	s.listen(3)
	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				print('Client from : ' + str(s_addr))
				p = Process(target=process_start, args=(s_sock,))
				p.start()

			except socket.error:
				print('SOCKET ERROR!')

	except Exception as e:
		print("INTERRUPT!")
		print(e)
		sys.exit(1)
	finally:
		s.close()