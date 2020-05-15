from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

keyboard = Controller()

password = ['D', 'r', '.', ' ', 'C', 'h', 'e', 'r', 'r', 'y', ' ', 'i', 's', ' ', 'i', 'n', ' ', 't', 'h', 'i', 's', ' ', 'c', 'l', 'a', 's', 's', '.', 'Dr', 'r.', '. ', ' C', 'Ch', 'he', 'er', 'rr', 'ry', 'y ', ' i', 'is', 's ', ' i', 'in', 'n ', ' t', 'th', 'hi', 'is', 's ', ' c', 'cl', 'la', 'as', 'ss', 's.']


timing = ['0.49', '0.19', '0.93', '0.43', '0.93', '0.90', '0.96', '0.35', '0.55', '0.95', '0.37', '0.85', '0.48', '0.44', '0.68', '0.28', '0.41', '0.82', '1.00', '0.68', '0.34', '0.43', '0.63', '0.24', '0.30', '0.46', '0.42', '0.89', '0.22', '0.17', '0.14', '0.70', '0.25', '0.42', '0.46', '0.51', '0.69', '0.95', '0.49', '0.44', '0.20', '0.78', '0.30', '0.12', '0.62', '0.72', '0.25', '0.80', '0.38', '0.43', '0.53', '0.23', '0.75', '0.40', '0.32']







password = password[:len(password) / 2 + 1]
password = "".join(password)

timing = [float(a) for a in timing]

keypress = timing[:len(timing) / 2 + 1]
keyintervals = timing[len(timing) / 2 + 1:]

#print keypress
#print keyintervals

i = 0
sleep(5)

for char in password:
    keyboard.press(char)
    sleep(keypress[i])
    keyboard.release(char)
    sleep(keyintervals[i%len(keyintervals)]) #delay going from one character to another
    i+=1 #go to the next timings

keyboard.press(Key.enter)
keyboard.release(Key.enter)

tcflush(stdin, TCIFLUSH)
print
