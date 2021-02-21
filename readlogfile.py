import time

#this short script continuously updates the output stream with data from the CAN data log, it will be expanded to update string variables with new CAN information

file = open("myfile.log","r")

while 1:
    where = file.tell() #logs location where we are in file 
    line = str(file.readline()) #takes line and turns into a string
    x = line.partition(" vcan0 ")
    y = x[2].partition("#")
   # node3 = line.find('001#') #node = 3
   # node2 = line.find('010#') #node = 2
   # node1 = line.find('100#') #node = 1

    if not line:
        time.sleep(1) #sleep mode (t); where t is a number in seconds
        file.seek(where) #where to go
    else:
       # print line, # already has newline
	#print(x)
	print(y[0])
	print(y[2])
