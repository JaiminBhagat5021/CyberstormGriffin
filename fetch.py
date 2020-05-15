#########################################################################################################
# Name: Jaimin Bhagat
# Date: 4/1/2020
# Description: Accessing an FTP server, then fetching file listing, decoding based on file permissions
#               using 2 methods, for method 7 ignore first 3 in file permissions
#               for method 10, include all 10 characters in file permissions (Done in Python 2.7.17)
#########################################################################################################

from ftplib import FTP #import FTP from library ftplib

# the FTP method
METHOD = 10

# globals (FTP specifics)
IP = "jeangourd.com"
PORT = 21
FOLDER = "10"

#the file/folder contents
contents = []
cutofstring = []
individual = []

# connect to the FTP server on the specified IP address and port, navigate
#to a specified folder, fetch a file listing, and disconnect
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

def decode(binary, n): #takes binary and some number of bits as parameters
    text = ""
    i = 0
    while(i < len(binary)):
        byte = binary[i:i+n] #Isolate a byte with n number of bits
        byte = int(byte, 2) #convert each byte of 1's and 0's to int in base 2
        if(byte > 127):
            byte = 00
        if(byte == 8): #if character is a backspace
            text = text[:-1] #remove last character of the string stored in text
        else:
            text += unichr(byte) #convert each ASCII value to its character version

        i += n
    return text


for row in contents:
    cutofstring.append(row[0:10]) #Get only the first 10 characters of each line in contents

#for method 7, remove all lines that have d in index 0, r in index 1, and w in index 0
#then add split each character individually and add it to list individual
if(METHOD == 7):
    i = 0
    for item in cutofstring:
        if(item[i+1] == 'r'):
            cutofstring.remove(item)
    for item in cutofstring:
        if(item[i+2] == 'w'):
            cutofstring.remove(item)
    for item in cutofstring:
        if(item[i] == 'd'):
            cutofstring.remove(item)
    for item in cutofstring:
        for character in item:
            individual.append(character)

#for method 10, don't remove any lines, just split each character individually and add it to list individual
if(METHOD == 10):
    for item in cutofstring:
        for character in item:
            individual.append(character)

binary = ''
#check each character in list individual and assign 1's or 0's depending on what the character is. (drwx - 1, dash - 0)
for i in individual:
    if(i=='d'):
        binary+=str(1)
    if (i == 'r'):
        binary +=str(1)
    if(i == 'w'):
        binary +=str(1)
    if(i == 'x'):
        binary +=str(1)
    if (i == '-'):
        binary +=str(0)

text = decode(binary, 7) #get the result of decode function and store it in text
print "7 bit:"
print text

text = decode(binary, 10) #get the result of decode function and store it in text
print "10 bit:"
print text
