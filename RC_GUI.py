import time
import tkinter as tk
import os

#os.system("candump -L vcan0 > myfile.log")

window = tk.Tk()
file = open("myfile.log","r")

greeting = tk.Label(text = "hello world")
greeting.pack()



while 1:
	os.system("candump -L vcan0 > myfile.log")
	time.sleep(1)
	#os.system("^C")	
#file = open('myfile.log', 'r')
	#f_contents = file.read()

	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" vcan0 ")
	y = x[2].partition("#")
    #greeting = tk.Label(text = str(y[0]))
    #print(y[0])
    #greeting = tk.Label(text = y[2])
    #greeting.pack()
    #window.update_idletasks()
    #window.update()

    #file.close()
   # node3 = line.find('001#') #node = 3
   # node2 = line.find('010#') #node = 2
   # node1 = line.find('100#') #node = 1

	if not line:
		#os.system("clear")
		time.sleep(1) #sleep mode (t); where t is a number in seconds
		file.seek(0) #where to go
	else:
       # print line, # already has newline
       # print(x)
		os.system("clear")
		print(y[0])
		print(y[2])
		
	#greeting = tk.Label(text = str(y[0]))
    #print(y[0])
    #greeting = tk.Label(text = y[2])
	#greeting.pack()
	#window.update_idletasks()
	#window.update()
	#file.close()
	#print("Closed file")
	ID = tk.Label(text = y[0])
	Msg = tk.Label(text = y[2])
	ID.pack()
	Msg.pack()
  
	window.update_idletasks()
	window.update()
    #tk.update_idletasks()
    #tk.update()
   # window.mainloop()


