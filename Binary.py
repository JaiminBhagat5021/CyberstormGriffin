###########################################################################################
# Name: Jaimin Bhagat
# Date: 3/23/2020
# Description: Binary Decoder for Bits evenly divisible by 7 and 8(Done in Python 2.7.17)
###########################################################################################

from sys import stdin #standard input library

def decode(binary, n): #takes binary and some number of bits as parameters
    text = ""
    i = 0
    while(i < len(binary)):
        byte = binary[i:i+n] #Isolate a byte with n number of bits
        byte = int(byte, 2) #convert each byte of 1's and 0's to int in base 2
        if(byte == 8): #if character is a backspace
            text = text[:-1] #remove last character of the string stored in text
        else:
            text += chr(byte) #convert each ASCII value to its character version

        i += n
    return text

#read input and get rid of the new line and store it in a variable
binary = stdin.read().rstrip("\n")


if(len(binary) %7 == 0): #length of binary is evenly divisible by 7
    text = decode(binary, 7) #get the result of decode function and store it in text
    print "7-bit:"
    print text
if(len(binary) %8 == 0): #length of binary is evenly divisible by 8
    text = decode(binary, 8) #get the result of deocde function and store it in text
    print "8-bit:"
    print text
