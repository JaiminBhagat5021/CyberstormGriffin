######################################################################################################
# Name: Jaimin Bhagat
# Date: 4/23/2020
# Description: XOR crypto method, takes a message(plain text or cipher text) and a key and XOR's them
               #producing an XOR cipher or decipher (Done in Python 2.7.17)
######################################################################################################

import sys #import libraries

KEY = "key" #file to read the key from
text = sys.stdin.read().rstrip("\n") #read standard input, without the new line

key = bytearray(open(KEY).read()) #open key file and read it as a byte array object
text = bytearray(text) #take text and store it as a byte array oject

result =[] #empty array
# XOR between the files
#For loop until there's data in text
for i in range(len(text)):
    result.append(key[i%len(key)]^text[i]) #wrap around the key incases where text is longer

print (bytearray(result)) #print each corresponding ASCII character
