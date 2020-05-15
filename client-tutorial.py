#########################################################################################################
# Name: Jaimin Bhagat
# Date: 4/14/2020
# Description: Connect to a chat server, get an overt message, and output a covert messaged based on time delays
#			  (Done in Python 2.7.17)
#########################################################################################################

#important standard librariers
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False
ZERO = 0.025
ONE = 0.1

# set the server's IP address and port
ip = "localhost"
port = 1320

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
covert_bin = ""
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	if (delta >= ONE): #if the delay is greater than .1 second
		covert_bin += "1" #add a 1 to the convert_bin
	else: #if the delay any other than .1 second(0.025 in this case)
		covert_bin += "0" #add a 0 to the covert_bin

	if (DEBUG): #debug mode
		stdout.write(" {}\n".format(delta)) #shows the time difference
		stdout.flush()

#close connection to the server
s.close()

covert = ""
i = 0

while (i < len(covert_bin)): #go through covert_bin 8 bits at a time
	#process one byte at a time
	b = covert_bin[i:i+8]
	#covert it to ASCII
	n = int("0b{}".format(b),2)
	try:
		covert +=unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	i+=8 #increment i by 8

print ("\nCovert message: " + covert)
