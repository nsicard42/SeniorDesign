import time
#import tkinter as tk
from tkinter import *
from tkinter import ttk
import os



#window = tk.Tk()
file = open("myfile.log","r")

#greeting = tk.Label(text = "hello world")
#greeting.pack()
root = Tk()
root.title('RC_GUI')
root.geometry("800x800")
root.resizable(0,0)

# create a main fram
#main_frame =ttk.Frame(root)
#main_frame.pack_propagate(0)
#main_frame.pack(fill=BOTH, expand=1)

# create a canvas
#my_canvas = Canvas(main_frame)
#my_canvas.pack_propagate(0)
#my_canvas.pack (side=LEFT, fill=BOTH, expand=1)

# add a scrollbar to the canvas
#my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command=my_canvas.yview)
#my_scrollbar.pack(side=RIGHT, fill=Y)


# configure the canvas
#my_canvas.configure(yscrollcommand=my_scrollbar.set)
#my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# create another frame in the canvas
#second_frame = Frame(my_canvas)

#add that frame to a window in canvas
#my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#root.mainloop()
while 1:
	os.system("timeout 1s candump -L vcan0 > myfile.log")
	

	# create a main fram
	#main_frame = Frame(root)
	#main_frame.pack(fill=BOTH, expand=1)

	# create a canvas
	#my_canvas = Canvas(main_frame)
	#my_canvas.pack (side=LEFT, fill=BOTH, expand=1)

	# add a scrollbar to the canvas
	#my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command=my_canvas.yview)
	#my_scrollbar.pack(side=RIGHT, fill=Y)

	# configure the canvas
	#my_canvas.configure(yscrollcommand=my_scrollbar.set)
	#my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

	# create another frame in the canvas
	#second_frame = Frame(my_canvas)

	#add that frame to a window in canvas
	#my_canvas.create_window((0,0), window=second_frame, anchor="nw")


	where = file.tell() #logs location where we are in file
	line = str(file.readline()) #takes line and turns into a string
	x = line.partition(" vcan0 ")
	y = x[2].partition("#")

	if not line:
                time.sleep(1) #sleep mode (t); where t is a number in seconds
                file.seek(0) #where to go
	else:
		os.system("clear")
		#if y[0]==0x80:
			#y[0] = "Headlight"
		#elif y[0]==0x01:
			#y[0] = "Gas Gauge"
		#else:
			#y[0] = "Speedometer"
		print(y[0])
		print(y[2])

	ID = Label(text = y[0]) #ID = tk.Label(text = y[0])
	Msg = Label(text = y[2]) #ID = tk.Label(text = y[2])
	ID.pack()
	Msg.pack()

	second_frame.update_idletasks() #root.update_idletasks()
	second_frame.update() #root.update()

