import time

#this short script continuously updates the output stream with data from the CAN data log, it will be expanded to update string variables with new CAN information

file = open("myfile.log","r")

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print line, # already has newline
