import serial
import time

uart_channel = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout=2)
running = True

#data1 = ""
#data = ""
#while 1:
#	data = uart_channel.read(1)
#	data1+=data
#	print(data)
#	uart_channel.flush()
#	data = ""
#	data1 = ""
#############################################

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
		#print(data)
		#print(data1)
		uart_channel.flush()
		if data.decode("utf-8") == '>':
			found = True
		data = ""
	return data1

while running:
	cmd = get_message()
	print(cmd)
