import os, time, shutil, colorama, requests, json, re
from colorama import Fore
from mcstatus import JavaServer
from pwinput import pwinput
colorama.init()

# Shittiest login I ever made but k. I swear if someone doesn't log in i'm jumping out of my window.
validUser = "admin"
validPwd = "admin"

usedHelp = False
cmds = ['help', 'serverdata', 'exit']

logo = """

*             (                         )                  
(  `      (     )\ )                   ( /(                  
)\))(     )\   (()/(         )         )\())   (     )  (    
((_)()\  (((_)   /(_)) (   ( /(   (    ((_)\   ))\ ( /(  )(   
(_()((_) )\___  (_))   )\  )(_))  )\ )  _((_) /((_))(_))(()\  
|  \/  |((/ __| / __| ((_)((_)_  _(_/( | \| |(_)) ((_)_  ((_) 
| |\/| | | (__  \__ \/ _| / _` || ' \))| .` |/ -_)/ _` || '_| 
|_|  |_|  \___| |___/\__| \__,_||_||_| |_|\_|\___|\__,_||_|   
                                                            
"""

def printcenter(s):
    for i in s.split('\n'):
        print(i.center(shutil.get_terminal_size().columns))

def removecolor(s):
    cc = ['§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f', '§k', '§l', '§m', '§n', '§o', '§r', '§A', '§B', '§C', '§D', '§E', '§F', '§K', '§L', '§M', '§N', '§O', '§R']

    for c in cc:
        s = s.replace(c, '')
    
    return s

def replacecolor(s):
    cc = ['§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f', '§k', '§l', '§m', '§n', '§o', '§r', '§A', '§B', '§C', '§D', '§E', '§F', '§K', '§L', '§M', '§N', '§O', '§R']
    ccr = [Fore.LIGHTBLACK_EX, Fore.BLUE, Fore.LIGHTGREEN_EX, Fore.CYAN, Fore.RED, Fore.MAGENTA, Fore.YELLOW, Fore.LIGHTBLACK_EX, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, '', '', '', '', '', '', Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, '', '', '', '', '', '']
    n = 0

    for c in cc:
        s = s.replace(c, '{}'.format(ccr[n]))
        n += 1

    return s
    
def main():
    os.system('cls || clear')
    print(Fore.RED, end="")
    printcenter(logo)
    print(Fore.RED + "Use the 'help' command to check out my commands.")
    print(Fore.RED + "https://github.com/TheBraisFP/MC-ScanNear")
    while True:
        option = input(f"{Fore.GREEN}[~] {Fore.RESET}")
        if option == "help":
            usedHelp = True
            print(f'  {Fore.BLUE}• {Fore.RESET}Project made by https://github.com/TheBraisFP/MC-ScanNear')
            print()
            print(f'  {Fore.RED}• {Fore.RESET}help')
            print("    Show's this message.")
            print()
            print(f'  {Fore.RED}• {Fore.RESET}serverdata <server>')
            print("    Get's data such as the MOTD, Version (protocol included) and more.")
            print()
        args = option.split()
        cmd = args[0]
        if cmd == "serverdata":
            if len(args) != 2:
                print(f'  {Fore.RED}•  {Fore.RESET}Usage: serverdata <ip/ip:port>')
                if not usedHelp:
                    print(f"  {Fore.BLUE}•  {Fore.RESET}If you want to know what commands there are. Use 'help'.")
            else:
                loaded = json.loads(requests.get(f'https://api.mcsrvstat.us/2/{args[1]}').text)
                try:
                    server = f'{loaded["ip"]}:{str(loaded["port"])}'
                    data = JavaServer.lookup(server).status()
                    motd = data.description
                    cmotd = removecolor(motd)
                    motd = replacecolor(motd)
                    version = data.version.name
                    cversion = removecolor(version)
                    version = removecolor(version)
                    protocol = data.version.protocol
                    connected_players = data.players.online
                    player_limit = data.players.max
                    if data.players.sample is not None:
                        players = str([f'{player.name} ({player.id})' for player in data.players.sample])
                        players = players.replace('[', '').replace(']', '').replace("'", '').replace('(00000000-0000-0000-0000-000000000000),', '').replace('(00000000-0000-0000-0000-000000000000)', '')
                        players = replacecolor(players)
                        re.findall(r'[0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z]-[0-9a-z][0-9a-z][0-9a-z][0-9a-z]-[0-9a-z][0-9a-z][0-9a-z][0-9a-z]-[0-9a-z][0-9a-z][0-9a-z][0-9a-z]-[0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z]', players)
                    else:
                        players = "No players online."
                    print(f'  {Fore.GREEN}• {Fore.RESET}Data found! Showing...')
                    print()
                    print(f'  {Fore.RED}MOTD: {Fore.RESET}\n{motd}')
                    print(f'  {Fore.RED}Version: {Fore.RESET}{version} (Protocol: {protocol})')
                    if players != "No players online.":
                        print(f'  {Fore.RED}Players: {Fore.RESET}{players}/{player_limit}')
                    else:
                        print(f'  {Fore.RED}Players: {Fore.RESET}{players}')
                except Exception as e:
                    print(f'  {Fore.RED}• {Fore.RESET}Invalid server, is the IP correct or does the server exist?')
            print()
        elif cmd == "exit":
            print(f"{Fore.RED}Thanks for using MC ScanNear.")
            time.sleep(3)
            exit()
        if not cmd in cmds:
            print(f"{Fore.RED}Invalid command.")
            time.sleep(3)
            main()

os.system("cls || clear")
print(Fore.RED, end="")
printcenter(logo)
print()
user = input('[~] Insert your username: ')
pwd = pwinput('[~] Insert your password: ')
if (user.lower() == validUser.lower() and pwd == validPwd):
    main()
else:
    print(Fore.RED+"Too bad to not read the source code.")
    exit()
