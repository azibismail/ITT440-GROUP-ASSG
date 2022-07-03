import socket
import signal
import sys


cSocket = socket.socket()
host = 'server ip'
port = 8888

print('Waiting')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))

Response = cSocket.recv(2048)
print(Response.decode("utf-8"))

print ("Book List\n");

print("A. Bisik Ombak Gelora\n")
print("B. Nasi Lemak Untuk Emak\n")
print("C. Mathematics for Dummies\n")
print("D. English for Dummies\n")
print("E. Kau Yang Terindah\n")
print("F. Hanya Kita Sahaja\n")
print("G. Firdaus Untuk Melur\n")
print("H. Hanya Melur\n")
print("I. Jangan Baca Buku Ini\n")
print("J. Cubaan 1..2..3!\n")

while True:
    opt = input('\nPlease input the book code (case sensitive). Type "EX" when you are done.\n')

    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G" or opt == "H" or opt == "I" or opt == "J":
        qty = input("Quantity: ")
        prc = '0'
        Input = opt + ":" + qty + ":" + prc
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

    elif opt == 'EX':
        print('Your order has been taken.\n')
        break

    else:
        print("Invalid. Try again.")
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(1024)
        print(Response.decode("utf-8"))

cSocket.close()
