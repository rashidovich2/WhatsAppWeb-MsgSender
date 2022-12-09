import pywhatkit as kit
import pyautogui as pg

try:
  kit.sendwhatmsg("+91xxxxxxxxxx", "message to send", 20,45) #08:45 IST

  #! 1st argument is the mobile number (write the mobile number with country code and without putting space in between the numbers Eg: +91xxxxxxxxxx)
  #! 2nd argument is the message to send
  #! 3rd argument is the time to send the message in 24hr format (if the time is 1:05 IST then we have to write it as 13,5 no need of adding 0 as prefix to minute. Try to give 4,5 minutes from the present time)

  pg.press("enter")
  print("Your message has successfully sent!")
except:
  print("exception error")