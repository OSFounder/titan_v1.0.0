import os
import sys
import time
import socket
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

try:
  import requests
  from PIL import Image, TkImage
except(ImportError):
  os.system('python3 -m pip install requests')
  import requests
  from PIL import Image, TkImage

bg_color = 'white'
fg_color = 'black'

win_main = Tk()
win_main.attributes('-zoomed', True, '-fullscreen', True)
win_main.config(bg=bg_color, fg=fg_color)
win_main.geometry('1000x850')
win_main.title('Nexus Titan')

term_frame = Frame(win_main, bg=bg_color)
terminal = Text(term_frame, bg=bg_color, fg=fg_color, height=100, width=50)
terminal.pack()
term_frame.pack()

class prompt:
  def get_cmd():
    rMsg = str(terminal.get(1.0, END))
    nLines = 0
    i = 0
    lMsg = list(rMsg)
    rslt = ''
    for char in lMsg:
      if char != '\n':
        pass
      else:
        nLines += 1
    
    for char in lmsg:
      if char != '\n':
        if i == nLines:
          rslt += str(char)
        else:
          pass
      else:
        if 1 == nLines:
          pass
        else:
          i += 1
          
      return rslt

  def proc_cmd():
    pass

win_main.mainloop()
