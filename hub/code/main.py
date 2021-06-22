#importing libraries
import serial
import time

#setting uart 
uart_channel = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout=2)
running = True

debug = False

def cur_ms():
	#gets current time in milliseconds
	return round(time.time())

def get_message():
	data1 = ""
	data = ""
	found = False
	while not found:
		data = uart_channel.read(1)
		data1 += data.decode("utf-8")
		if debug: #change debug to True to you know.... get debugging info
			print(data)
			print(data1)
		uart_channel.flush()
		if data.decode("utf-8") == '>': #wait for end or transmission sign
			found = True
		data = ""
	return data1

while running: #just testing to see if it works right now it only spits out what it finds
	cmd = get_message()
	print(cmd)

