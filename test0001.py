from test0002 import *
import time
import sys
import os
import os.path
import pickle
import json


sys_save_yn = input("[SYSTEM]Do you want to get back to the last save point (if you never reached a save point, enter n)? (y/n)")
while True:
    if sys_save_yn.lower() in  ("yes", "y"):
        saveload()
    elif sys_save_yn.lower() in  ("no", "n"):
        break
    else:
        print("[SYSTEM]Incorrect input ! Try again\n")

room_all()
