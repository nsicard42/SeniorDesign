import time
import tkinter as tk
import os



window = tk.Tk()
file = open("myfile.log","r")

greeting = tk.Label(text = "hello world")
greeting.pack()



while 1:
	os.system("candump -L vcan0 > myfile.log")
	time.sleep(1)

	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" vcan0 ")
	y = x[2].partition("#")

	if not line:
		time.sleep(1) #sleep mode (t); where t is a number in seconds
		file.seek(0) #where to go
	else:
		os.system("clear")
		print(y[0])
		print(y[2])

	ID = tk.Label(text = y[0])
	Msg = tk.Label(text = y[2])
	ID.pack()
	Msg.pack()

	window.update_idletasks()
	window.update()


