######################################################################################################
# Name: Jaimin Bhagat
# Date: 4/11/2020
# Description: Hashing a specific time difference twice, getting 2 alphabetic characters left to right,
    #Getting 2 numeric characters right to left and printing out result (Done in Python 2.7.17)
######################################################################################################
#import standard libraries
from datetime import datetime
import pytz
from sys import stdin
import hashlib
from datetime import timedelta

# debug mode?
DEBUG = False

# set to True if on the challenge server
ON_SERVER = False

# valid time interval
INTERVAL = 60
# manual current datetime?
MANUAL_DATETIME = "2015 01 01 00 00 35"

local_time = pytz.timezone("America/Chicago")

#Get epoc time from user
epoch = stdin.read().rstrip("\n") #Gets rid of the new line

if(MANUAL_DATETIME == ""): #If no time is entered
    current = datetime.now() #Get the current time
    #Localize that current time to America/Chicago
    current = local_time.localize(current, is_dst=True)
    #Convert that time to UTC
    utc_datetime = current.astimezone(pytz.utc)


else:
    #Take a string and convert it to date time object based on the specified format
    MANUAL_DATETIME = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
    #Format the date time in the specified format
    MANUAL_DATETIME.strftime("%Y-%m-%d %H:%M:%S")
    #Localize time to America/Chicago
    local_datetime = local_time.localize(MANUAL_DATETIME)
    #Covert to UTC times
    utc_datetime = local_datetime.astimezone(pytz.utc)

#Same process, get epoch time in correct format, localize it, and convert to UTC
epoch = datetime.strptime(epoch, "%Y %m %d %H %M %S")
epoch.strftime("%Y-%m-%d %H:%M:%S")
epoch_local_datetime = local_time.localize(epoch, is_dst=True)
epoch_utc_datetime = epoch_local_datetime.astimezone(pytz.utc)

#Keep the code valid for the specified interval, then update it
second_difference = (utc_datetime.second-epoch_utc_datetime.second)
New_seconds = ((second_difference+INTERVAL)%INTERVAL)
difference = (utc_datetime-epoch_utc_datetime)
total_seconds = int(difference.total_seconds())
time_elapsed = (total_seconds-New_seconds)

#hash it once using md5
hash1 = hashlib.md5(str(time_elapsed)).hexdigest()

#hash the previous hash again using md5
hash2 = hashlib.md5(hash1).hexdigest()
password = ""

#First get 2 alphabetic characters, left to right
for i in hash2:
    if(i.isalpha()):
        password+=i
    if(len(password) == 2):
        break
#Reverse the hash string
reversed_hash = hash2[::-1]
#Get 2 numeric characters, right to left
for i in reversed_hash:
    if(i.isdigit()):
        password+=i
    if(len(password) == 4):
        break
print password

#Debug mode
if(DEBUG == True):
    print "current system time: " + str(utc_datetime)
    print "current epoch time: "  + str(epoch_utc_datetime)
    print "Without interval = " + str(total_seconds)
    print "Actual elasped time = " + str(time_elapsed)
    print "Hash1 = " + str(hash1)
    print "Hash2 = " + str(hash2)
