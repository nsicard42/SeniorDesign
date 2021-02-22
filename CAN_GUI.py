import time
import tkinter as tk
import os

window = tk.Tk()
file = open("myfile.log","r")

greeting.pack()
node1 = "xxx"
node2 = "xxx"
node3 = "xxx"

while 1:
	os.system("timeout 1s candump -L can0 > myfile.log")

	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" can0 ")
	y = x[2].partition("#")
	
	if not line:
		time.sleep(1) #sleep mode (t); where t is a number in seconds
		file.seek(0) #where to go
	else:
		os.system("clear")
		if (y[0] == "080"):
			node1 = y[2]
		else if (y[0] == "010"):
			node2 = y[2]
		else if (y[0] == "F67"):
			node3 = y[2]
			
		print("node 1: ", node1)
		print("node 2: ", node2)
		print("node 3: ", node3)
		
	ID = tk.Label(text = y[0])
	Msg = tk.Label(text = y[2])
	ID.pack()
	Msg.pack()
  
	window.update_idletasks()
	window.update()
	

