from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout


keyboard = Controller()

password = ['D', 'r', '.', ' ', 'C', 'h', 'e', 'r', 'r', 'y', ' ', 'i', 's', ' ', 'i', 'n', ' ', 't', 'h', 'i', 's', ' ', 'c', 'l', 'a', 's', 's', '.', 'Dr', 'r.', '. ', ' C', 'Ch', 'he', 'er', 'rr', 'ry', 'y ', ' i', 'is', 's ', ' i', 'in', 'n ', ' t', 'th', 'hi', 'is', 's ', ' c', 'cl', 'la', 'as', 'ss', 's.']
timings = ['1.00', '0.43', '0.70', '0.62', '0.50', '0.20', '0.85', '0.58', '0.53', '0.25', '0.74', '0.66', '0.82', '0.76', '0.93', '0.87', '0.35', '0.37', '1.00', '0.58', '0.26', '0.41', '0.25', '0.61', '0.91', '0.99', '0.80', '0.74', '0.19', '0.37', '0.19', '0.91', '0.78', '0.39', '0.55', '0.12', '0.60', '0.95', '0.78', '0.22', '0.82', '0.79', '0.83', '0.56', '0.55', '0.95', '0.68', '0.79', '0.49', '0.64', '0.25', '0.36', '0.96', '0.53', '0.77']



password = password[:len(password) / 2 + 1]
password = "".join(password)


timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2 + 1]
keyintervals = timings[len(timings) / 2 + 1 :]

i = 0
sleep(5) #delay that allows to change focus
for char in password:  #for every character in password
    keyboard.press(char) #press character
    sleep(keypress[i]) #delay of character key behing held
    keyboard.release(char) #release character
    sleep(keyintervals[i%len(keyintervals)]) #delay going from one character to another
    i+=1 #go to the next timings

tcflush(stdout, TCIFLUSH)
print
