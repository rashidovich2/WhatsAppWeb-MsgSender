import pywhatkit as kit
import pyautogui as pg

try:
  kit.sendwhatmsg("+917306333244", "hai monee...",13,18)
  # 1st argument is the number, 2nd: message, 3rd: time in hr and min 24 format (if the time is 1:05 IST then we have to write it as 13:5, no need of adding 0 as prefix to min. Try to give 4,5 min from the present time)
  pg.press("enter")
except:
  print("exception error")