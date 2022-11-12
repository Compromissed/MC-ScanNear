from requests import get, exceptions
import time
import colorama
from colorama import Fore
import os

respuesta_si = "yes"

serverlogo = """


   _____                             _____                 
  / ____|                           / ____|                
 | (___   ___ _ ____   _____ _ __  | (___   ___ __ _ _ __  
  \___ \ / _ \ '__\ \ / / _ \ '__|  \___ \ / __/ _` | '_ \ 
  ____) |  __/ |   \ V /  __/ |     ____) | (_| (_| | | | |
 |_____/ \___|_|    \_/ \___|_|    |_____/ \___\__,_|_| |_|
                                                           
                                                           


"""

print(Fore.RED + serverlogo)

print(Fore.BLUE + "Welcome to the ScanNear servers options")

go_on = input(Fore.CYAN + "Do you want to continue?: ")
if go_on == respuesta_si:
    pass
else:
    print(Fore.RED + "Ok. Returning to the main page")
    print(Fore.GREEN + "Made by TheBraisFP")
    time.sleep(2)
    os.system("cls")
    os.system("python main.py")

serv = input("What server are you going to scan?: ")
print(Fore.BLUE + "Scanning server...")
os.system(f"ping {serv} -n 1")
print(Fore.RED + "This are the results")
print(Fore.GREEN + "Made by TheBraisFP")
time.sleep(3)

home_scan = input(Fore.RED + "Do you want to scan more servers?: ")

if home_scan == respuesta_si:
    print(Fore.RED + "Wait a few seconds")
    print(Fore.GREEN + "Made by TheBraisFP")
    time.sleep(2)
    os.system("cls")
    os.system("python server.py")
else:
    print(Fore.RED + "Ok. Returning to the main page")
    time.sleep(2)
    os.system("cls")
    os.system("python main.py")
    






#except exceptions.ConnectionError:
        #print(Fore.RED + "Servidor offline o problemas de conexión")

