import os
import getpass
import sys, shutil, colorama
from colorama import Fore
colorama.init()


logo = """

  __  __         _____                 _   _                 
 |  \/  |       / ____|               | \ | |                
 | \  / | ___  | (___   ___ __ _ _ __ |  \| | ___  __ _ _ __ 
 | |\/| |/ __|  \___ \ / __/ _` | '_ \| . ` |/ _ \/ _` | '__|
 | |  | | (__   ____) | (_| (_| | | | | |\  |  __/ (_| | |   
 |_|  |_|\___| |_____/ \___\__,_|_| |_|_| \_|\___|\__,_|_|   
                                                                                                                                                                            
                                                             

"""

print(Fore.RED + logo)

usuario = "admin"
contra = "admin"

for i in range(2):
    user = input(Fore.WHITE + "Username: ")
    if user == usuario:
        for i in range(2):
            password = getpass.getpass(Fore.WHITE + "Password: ")
            if password == contra:
                print(Fore.GREEN + "Just logged in")
                os.system("cls")
                os.system("python main.py")
                sys.exit()

            else:
                print(Fore.RED + "Password error")
                sys.exit()
    else:
        print(Fore.RED + "Username error")

