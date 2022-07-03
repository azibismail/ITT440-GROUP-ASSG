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
