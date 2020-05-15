from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

keyboard = Controller()

string = "this is a really long string that someone is typing out"

for char in string:
    keyboard.press(char)
    sleep(uniform(0.02, 0.3))
    keyboard.release(char)

tcflush(stdin, TCIFLUSH)
print
