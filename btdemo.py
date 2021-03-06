import os
import glob
import time
import bluetooth
import RPi.GPIO as GPIO
	
node1="xxx"
node2="xxx"
node3="xxx"
	
file = open("myfile.log","r")
	
forward_pin = 40
reverse_pin = 38
left_pin = 36
right_pin = 32
pin_state = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(reverse_pin, GPIO.OUT)
GPIO.setup(left_pin, GPIO.OUT)
GPIO.setup(right_pin, GPIO.OUT)

#host = ""
#port = 1

GPIO.output(forward_pin, pin_state)
GPIO.output(reverse_pin,pin_state)
GPIO.output(left_pin, pin_state)
GPIO.output(right_pin, pin_state)

def toggle_forward_on():
	GPIO.output(forward_pin, True)
	
def toggle_forward_off():
	GPIO.output(forward_pin, False)

def toggle_reverse_on():
	GPIO.output(reverse_pin, True)
	
def toggle_reverse_off():
	GPIO.output(reverse_pin, False)
	
def toggle_left_on():
	GPIO.output(left_pin, True)
	
def toggle_left_off():
	GPIO.output(left_pin, False)

def toggle_right_on():
	GPIO.output(right_pin, True)
	
def toggle_right_off():
	GPIO.output(right_pin, False)

host = ""
port = 1

server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]
uuid = "ae14f5e2-9eb6-4015-8457-824d76384ba0"
bluetooth.advertise_service( server_sock, "raspberrypi", service_id = uuid, service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ]) 
               
while True:
	os.system("timeout 1s candump -L vcan0 > myfile.log")
	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" vcan0 ")
	y = x[2].partition("#")

	if not line:
                #time.sleep(1) #sleep mode (t); where t is a number in seconds
                file.seek(0) #where to go
	else:
		#if (y[0] == "080"): #Add in to test Node 1
		node1 = y[2]
		#elif (y[0] == "010"): #Add in to test Node2
		node2 = y[2]
		#else:
		node3 = y[2]

		print("node 1: ", node1) #Terminal Print.Remove
		print("node 2: ", node2) #Terminal Print.Remove
		print("node 3: ", node3) #Terminal Print.Remove

	print("Waiting for connection on RFCOMM channel %d" % port)

	client_sock, client_info = server_sock.accept()
	print ("Accepted connection from", client_info)
	try:
		data = client_sock.recv(1024)
		if len(data) == 0: break
		print ("received [%s]" % data)
		if data == "forward_press":
			send_data = "pressed#"
			toggle_forward_on()
			
		elif data == "forward_release":
			send_data = "released#"
			toggle_forward_off()
			
		elif data == "reverse_press":
			send_data = "pressed#"
			toggle_reverse_on()
			
		elif data == "reverse_release":
			send_data = "released#"
			toggle_reverse_off()
			
		elif data == "left_press":
			send_data = "pressed#"
			toggle_left_on()
			
		elif data == "left_release":
			send_data = "released#"
			toggle_left_off()
			
		elif data == "right_press":
			send_data = "pressed#"
			toggle_right_on()
			
		elif data == "right_release":
			send_data = "released#"
			toggle_right_off()
			
		elif data == "connect_request":
			send_data = "connected#"
			
		elif data == "disconnect_request":
			send_data = "disconected#"
		elif data == "node1":
			send_data = node1 + "#"
			
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
