import os
import glob
import time
import bluetooth
import RPi.GPIO as GPIO
	
	#this script was written as a test allowing for the GPIO to be controlled through bt with a corresponding application written in android studios
	
led_pin1 = 40
led_pin2 = 38
led_state = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
host = ""
port = 1
GPIO.output(led_pin1,led_state)
GPIO.output(led_pin2,led_state)

def toggle_led_on1():
	GPIO.output(led_pin1, True)
	
def toggle_led_off1():
	GPIO.output(led_pin1, False)

def toggle_led_on2():
	GPIO.output(led_pin2, True)
	
def toggle_led_off2():
	GPIO.output(led_pin2, False)

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
server_sock.bind(("",bluetooth.PORT_ANY))
print("Bluetooth Binding Completed")
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "ae14f5e2-9eb6-4015-8457-824d76384ba0"

bluetooth.advertise_service(server_sock,"raspberrypi",service_id = uuid, service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ] )

while True:
	print("Waiting for connection on RFCOMM channel %d" % port)

	client_sock, client_info = server_sock.accept()
	print ("Accepted connection from", client_info)
	try:
		data = client_sock.recv(1024)
		if len(data) == 0: break
		print ("received [%s]" % data)
		if data == "press2":
			send_data = "pressed#"
			toggle_led_on2()
		elif data == "release2":
			send_data = "released#"
			toggle_led_off2()
		elif data == "press1":
			send_data = "pressed#"
			toggle_led_on1()
		elif data == "release1":
			send_data = "released#"
			toggle_led_off1()
		elif data == "connect_request":
			send_data = "connected#"
		elif data == "disconnect_request":
			send_data = "disconected#"
		else:
			send_data = "\nInvalid Input\n"

		client_sock.send(send_data)
		print ("sending [%s]" % send_data)

	except IOError:
		pass

	except KeyboardInterrupt:
		
		print ("disconnected")
		
		client_sock.close()
		server_sock.close()
		print ("all done")

		break
