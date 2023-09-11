# Python program to send whatsapp message to a particular person according to the count given by the user

import pywhatkit as kit
import pyautogui as pg
import time

limit = int(input("Enter the number of limit: "))
message = input("Enter the message to send: ")
count = 0

try:
  kit.sendwhatmsg("+91XXXXXXXXXX", "message to send", 1,21) #1:21 IST

  #! 1st argument is the mobile number (write the mobile number with country code and without putting space in between the numbers Eg: +91XXXXXXXXXX)
  #! 2nd argument is the message to send
  #! 3rd argument is the time to send the message in 24hr format (if the time is 1:05 IST then we have to write it as 13,5 no need of adding 0 as prefix to minute. Try to give 4,5 minutes from the present time)

  print("Your 1st message has sent")

  time.sleep(2)

  while count <= limit:
    pg.typewrite(message)
    pg.press("enter")
    count += 1

except:
  print("Exception error")