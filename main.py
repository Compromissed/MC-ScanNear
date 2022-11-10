#Libraries
import getpass
import sys, shutil, colorama
from colorama import Fore
colorama.init()

def printcenter(s):
    print(s.center(shutil.get_terminal_size().columns))

#Logo

logo = """

  __  __         _____                 _   _                 
 |  \/  |       / ____|               | \ | |                
 | \  / | ___  | (___   ___ __ _ _ __ |  \| | ___  __ _ _ __ 
 | |\/| |/ __|  \___ \ / __/ _` | '_ \| . ` |/ _ \/ _` | '__|
 | |  | | (__   ____) | (_| (_| | | | | |\  |  __/ (_| | |   
 |_|  |_|\___| |_____/ \___\__,_|_| |_|_| \_|\___|\__,_|_|   
                                                                                                                                                                            
                                                             

"""
printcenter(Fore.RED + logo)

#Username


usuario = "admin"
contra = "admin"

for i in range(2):
    user = input(Fore.WHITE + "Username: ")
    if user == usuario:
        for i in range(2):
            password = getpass.getpass(Fore.WHITE + "Password: ")
            if password == contra:
                print(Fore.GREEN + "Just logged in")
                sys.exit()
            else:
                print(Fore.RED + "Password error")
                sys.exit()
    else:
        print(Fore.RED + "Username error")

print(Fore.BLUE + "Options to choose")


# Corregir bucles