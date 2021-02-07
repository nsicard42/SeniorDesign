import time

#this short script continuously updates the output stream with data from the CAN data log, it will be expanded to update string variables with new CAN information

file = open("myfile.log","r")

while 1:
    where = file.tell() #logs location where we are in file 
    line = file.readline() #takes line and turns into a string
    if not line:
        time.sleep(1) #sleep mode (t); where t is a number in seconds
        file.seek(where) #where to go
    else:
        print line, # already has newline
