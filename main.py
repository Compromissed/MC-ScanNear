#Libraries
import getpass
import os
import time
import sys, shutil, colorama
from colorama import Fore
colorama.init()


def printcenter(s):
    print(s.center(shutil.get_terminal_size().columns))

mainlogo = """



  _    _                      
 | |  | |                     
 | |__| | ___  _ __ ___   ___ 
 |  __  |/ _ \| '_ ` _ \ / _ |
 | |  | | (_) | | | | | |  __/
 |_|  |_|\___/|_| |_| |_|\___|
                              
                              
            

"""

scansv = "1"
exit = "2"

print(Fore.RED + mainlogo)

print(Fore.BLUE + "Options to choose: ")
print(Fore.RED + "1) Test servers")
print(Fore.RED + "2) Exit")
print(Fore.RED + "...")
option = input("Option: ")
if option == scansv:
    print("Wait a few seconds")
    time.sleep(1)
    os.system("cls")
    os.system("python server.py")
else:
    pass
if option == exit:
    print("Thanks for using MC ScanNear")
    time.sleep(1.5)
    os.system("TASKKILL /F /IM cmd.exe")



