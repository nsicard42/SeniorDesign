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

gasValue = "initializing"
Speed = 0
lightLevel = "initializing"




file = open("myfile.log","r")


root = Tk()
root.title('RC_GUI')
root.geometry("400x400")
root.resizable(0,0)

while 1:
	os.system("timeout 0.6s candump -L can0 > myfile.log")

	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" can0 ")
	y = x[2].partition("#")


	if not line:
                #time.sleep(1) #sleep mode (t); where t is a number in seconds
		file.seek(0) #where to go
	else:
                #os.system("clear")
		Msg1.destroy() #Allows the update of Message from node1
		Msg2.destroy() #Allows the update of Message from node2
		Msg3.destroy() #Allows the update of Message from node3

		if (y[0] == "080"): #Add in to test Node 1
			#print("Made it to if statement") #fixme.delete Test
			node1 = y[2]

			myList = list(y[2])
			myHex = "0x" + myList[0] + myList[1]
			myHexVal = int(myHex, 16)
			
			if (myHexVal == 0):
				Speed = 0

			elif (myHexVal > 0 and myHexVal <=1):
				Speed = 1

			elif (myHexVal > 1 and myHexVal <=2):
				Speed = 2

			elif (myHexVal > 2 and myHexVal <=3):
				Speed = 3

			elif (myHexVal > 3 and myHexVal <=4):
				Speed = 4

			elif (myHexVal > 4 and myHexVal <=5):
				Speed = 5

			elif (myHexVal > 5 and myHexVal <=6):
				Speed = 6

			elif (myHexVal > 6 and myHexVal <=7):
				Speed = 7

			elif (myHexVal > 7 and myHexVal <=8):
				Speed = 8

			elif (myHexVal > 8 and myHexVal <=9):
				Speed = 9

			else:
				Speed = 10

			#ID1 = Label(text = "Speedometer") #ID Node1 #FixME. ADD Proper Label Name
			#Msg1 = Label(text = str(Speed) + "m/s") #Message from Node1
			#ID1.grid(row=1, column=1)
			#Msg1.grid(row=1, column=2)

		elif (y[0] == "010"): #Add in to test Node2
			node2 = y[2]

			myList = list(y[2])
			myHex = "0x" + myList[0] + myList[1]
			myHexVal = int(myHex, 16)

			if (myHexVal <=4):
				gasValue = "full"
			elif (myHexVal <=10 and myHexVal >8):
				gasValue  = "1/4"
			elif (myHexVal <= 8 and myHexVal > 6):
				gasValue = "1/2"
			elif (myHexVal <=6 and myHexVal > 4):
				gasValue = "3/4"
			else:
				gasValue = "low"

			#ID2 = Label(text = "Gas") #ID Node2 #FixME. ADD Proper Label name
			#Msg2 = Label(text = gasValue) #Message from Node2
			#ID2.grid(row=2,column=1)
			#Msg2.grid(row=2,column=2)


		else:
			node3 = y[2]

			myList = list(y[2])
			myHex = "0x" + myList[0] + myList[1]
			myHexVal = int(myHex, 16)

			if (myHexVal == 0):
				lightLevel = "High Light"
			elif (myHexVal >0 and myHexVal <50):
				lightLevel = "Medium Light"
			else:
				lightLevel = "Low Light"

			#ID3 = Label(text = "Head Light") #ID Node3 #FixME. ADD Proper label Name
			#Msg3 = Label(text = lightLevel) #Message from Node3
			#ID3.grid(row=3,column=1)
			#Msg3.grid(row=3,column=2)

		ID1 = Label(text = "Speedometer") #ID Node1 #FixME. ADD$
		Msg1 = Label(text = str(Speed) + "m/s") #Message from N$
		ID1.grid(row=1, column=1)
		Msg1.grid(row=1, column=2)

		ID2 = Label(text = "Gas") #ID Node2 #FixME. ADD Proper $
		Msg2 = Label(text = gasValue) #Message from Node2
		ID2.grid(row=2,column=1)
		Msg2.grid(row=2,column=2)

		ID3 = Label(text = "Head Light") #ID Node3 #FixME. ADD $
		Msg3 = Label(text = lightLevel) #Message from Node3
		ID3.grid(row=3,column=1)
		Msg3.grid(row=3,column=2)


		print("node 1: ", node1) #Terminal Print.Remove
		print("node 2: ", node2) #Terminal Print.Remove
		print("node 3: ", node3) #Terminal Print.Remove

	root.update_idletasks() #Updates Window Information
	root.update() #Packs Update








