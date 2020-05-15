###########################################################################################
# Name: Jaimin Bhagat
# Date: 3/24/2020
# Description: Encryption and Decryption of a message with a key(Done in Python 2.7.17)
###########################################################################################
from sys import stdin, argv

#Empty lists
Indices_Text = []
Indices_Key = []
Value = []
Text = []

def encrypt(plaintext, key):
    key = ''.join(e for e in key if e.isalpha()) #takes the key and removes characters that are not alphabetic
    ciphertext = ''
    for i in range(len(plaintext)): #iterates through each character in plaintext
        if(not(plaintext[i].isalpha())): #if a character is not an alphabetic character
            Indices_Text.append(plaintext[i]) #then just append it as it is to the list Indices_Text
        else:
            if(plaintext.islower()): #if the character is already lower case
                Indices_Text.append(ord(plaintext[i])-97) #a-z range from 97 to 122, so subtract 97 to get a-0, b-1, c-2,...z-25
            else:
                Indices_Text.append(ord(plaintext[i].lower())-97) #when the alphabetic character is uppercase, lowercase it then perform calculations
    for i in range(len(key)):
        if(key.islower()):
            Indices_Key.append(ord(key[i])-97) #same calculations for the key as the text appended to a Indices_Key list
        else:
            Indices_Key.append(ord(key[i].lower())-97)
    #At this point, both Indices_Text and Indices_Key will have numeric values corresponding to each lowercase alphabetic character
    #For characters that were not alphabetic, they will be stored as a substring
    #a will correspond to 0, b will correspond to 1, .... z will correspond to 25

    for i in range(len(Indices_Text)): #iterate through list Indices_Text
        if(type(Indices_Text[i])!=int): #If the stored element in Indices_Text is not an integer
            Value.append(Indices_Text[i]) #Append it as it is to list Value
            Indices_Key.insert(0,Indices_Key.pop()) #Shift each element in Indices_Key to the right
        else:
            Value.append((Indices_Text[i]+Indices_Key[i%len(Indices_Key)])%26)
            #If stored element is an integer in Indices_Text then add it to the integer in Indices_Key and take the modulus of the summed Value
            #Also do a loop around of the key if the last element in Indices_Key is reached

    #At this point, the list Value will have integers that can be converted back to a corresponding character
    #It will also have substrings that can be maitained as they are

    for number in Value: #For each elements in list Value
        if(type(number)!=int): #If the type of the element is not integer, meaning it's a substring
            Text.append(number) #append it as it is to list Text
        else:
            Text.append(chr(((number)+97))) #If the element is an integer, add 97 to it and get the ASCII character for the decimal number
                                            #and append it to the list Text

    #At this point we will have the encrypted message of our text provided based on the key
    #However, the characters will all be lowercase

    #This for loop will compare the input text and match the case(uppercase/lowercase) in our encrypted Text,
    #and each character will be concatenated and stored as a string in ciphertext
    l = 0
    for element in plaintext:
        if(element.isupper()):
            ciphertext+=str(Text[l].upper())
            l+=1
        else:
            ciphertext+=str(Text[l])
            l+=1

    return ciphertext

#The process for decrpytion is similar to encryption, the only difference is Indices_Text and Indices_Key
#will be subtracted instead of added and 26 will be added to the difference of Indices_Key and Indices_Text to maintain positive integers
def decrypt(ciphertext, key):
    key = ''.join(e for e in key if e.isalpha())
    plaintext = ''
    for i in range(len(ciphertext)):
        if(not(ciphertext[i].isalpha())):
            Indices_Text.append(ciphertext[i])
        else:
            if(ciphertext.islower()):
                Indices_Text.append(ord(ciphertext[i])-97)
            else:
                Indices_Text.append(ord(ciphertext[i].lower())-97)
    for i in range(len(key)):
        if(key.islower()):
            Indices_Key.append(ord(key[i])-97)
        else:
            Indices_Key.append(ord(key[i].lower())-97)
    for i in range(len(Indices_Text)):
        if(type(Indices_Text[i])!=int):
            Value.append(Indices_Text[i])
            Indices_Key.insert(0,Indices_Key.pop())
        else:
            Value.append((26+(Indices_Text[i]-Indices_Key[i%len(Indices_Key)]))%26)
    for number in Value:
        if(type(number)!=int):
            Text.append(number)
        else:
            Text.append(chr(((number)+97)))
    l = 0
    for element in ciphertext:
        if(element.isupper()):
            plaintext+=str(Text[l].upper())
            l+=1
        else:
            plaintext+=str(Text[l])
            l+=1

    return plaintext



try:
    mode = argv[1] #Takes 2 arguments
    key = argv[2]
except IndexError: #If exactly 2 arguments are not provided then raise an exception
    print "Not enough arguments provided, Please re-run the program and provide 2 arguments(Mode & Key)."
    exit(0)

text = stdin.read().rstrip("\n") #Gets rid of the new line

if(mode == "-e"): #If the mode argument is -e then encrypt the message
    ciphertext = encrypt(text, key)
    print ciphertext

elif(mode == "-d"): #If the mode argument is -d then decrypt the message
    plaintext = decrypt(text, key)
    print plaintext
