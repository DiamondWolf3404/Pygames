from test0002 import *
import time
import sys
import os
import os.path
import pickle
import json



file_exists = os.path.isfile('savefile001.txt')
def saveload():
    if file_exists:
        file=open("savefile001.txt","r")
        checkpoint = file.read()
        file.close()
    else:
        checkpoint = "0"
        print("[SYSTEM]No savefile found")
        print("[SYSTEM]Would you like to go to checkpoint '1'?")
        sys_nosavefound_yn = input("[SYSTEM]Would you like to start from the beginning ? (y/n)\n")
        if sys_nosavefound_yn.lower() in  ("yes", "y"):
            room_all()
        else:
            print("[SYSTEM]Program finished\n")
            input("[SYSTEM]Press enter to exit")


def save():
    file=open("savefile001.txt","w")
    file.write()
    file.close()

def clear():
    os.system('cls')

def dprint001(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
def dprint002(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.50)
def dprint003(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.80)


def license():
    print("[SYSTEM]This work © 2022 by Diamond Wolf is licensed under CC BY-NC-SA 4.0")


sys_save_yn = input("[SYSTEM]Do you want to get back to the last save point (if you never reached a save point, enter n)? (y/n)")
while True:
    if sys_save_yn.lower() in  ("yes", "y"):
        saveload()
    elif sys_save_yn.lower() in  ("no", "n"):
        break
    else:
        print("[SYSTEM]Incorrect input ! Try again\n")
