# Python code to send a whatsapp message to a particular group

import pywhatkit as kit

try:
  kit.sendwhatmsg_to_group("groupid", "message to send", 23,23) #11:23 IST

  #! 1st argument is the group id Eg: FkUek3cSf7EIcE9Nzixmil
  #! 2nd argument is the message to send
  #! 3rd argument is the time to send the message in 24hr format (if the time is 1:05 IST then we have to write it as 13,5 no need of adding 0 as prefix to minute. Try to give 4,5 minutes from the present time)

  print("Your message has successfully sent!")
except:
  print("exception error")