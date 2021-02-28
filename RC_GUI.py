import time
from tkinter import *
from tkinter import ttk
import os

node1="xxx"
node2="xxx"
node3="xxx"
Msg1 = Label(text = "0") 
Msg2 = Label(text = "0") 
Msg3 = Label(text = "0") 



file = open("myfile.log","r")


root = Tk()
root.title('RC_GUI')
root.geometry("400x400")
root.resizable(0,0)

while 1:
	os.system("timeout 1s candump -L vcan0 > myfile.log")

	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" vcan0 ")
	y = x[2].partition("#")

	if not line:
                time.sleep(1) #sleep mode (t); where t is a number in seconds
                file.seek(0) #where to go
	else:
		os.system("clear")
		Msg1.destroy() #Allows the update of Message from node1
		Msg2.destroy() #Allows the update of Message from node2
		Msg3.destroy() #Allows the update of Message from node3

		#if (y[0] == "080"): #Add in to test Node 1
		node1 = y[2]
		ID1 = Label(text = "Funny sensor1") #ID Node1 #FixME. ADD Proper Label Name
		Msg1 = Label(text = y[2]) #Message from Node1
		ID1.grid(row=1, column=1)
		Msg1.grid(row=1, column=2)

		#elif (y[0] == "010"): #Add in to test Node2
		node2 = y[2]
		ID2 = Label(text = "Funny sensor2") #ID Node2 #FixME. ADD Proper Label name
		Msg2 = Label(text = y[2]) #Message from Node2
		ID2.grid(row=2,column=1)
		Msg2.grid(row=2,column=2)
		#else:
		node3 = y[2]
		ID3 = Label(text = "Funny sensor3") #ID Node3 #FixME. ADD Proper label Name
		Msg3 = Label(text = y[2]) #Message from Node3
		ID3.grid(row=3,column=1)
		Msg3.grid(row=3,column=2)


		print("node 1: ", node1) #Terminal Print.Remove
		print("node 2: ", node2) #Terminal Print.Remove
		print("node 3: ", node3) #Terminal Print.Remove

	root.update_idletasks() #Updates Window Information
	root.update() #Packs Update


