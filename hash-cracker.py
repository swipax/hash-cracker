import os
import hashlib
import time
from colorama import Fore, Style
import colorama
colorama.init()
os.system('cls' if os.name == 'nt' else 'clear') 


def banner():
    print(Fore.MAGENTA+"""
  _               _                               _    
 | |__   __ _ ___| |__         ___ _ __ __ _  ___| | __
 | '_ \ / _` / __| '_ \ _____ / __| '__/ _` |/ __| |/ /
 | | | | (_| \__ \ | | |_____| (__| | | (_| | (__|   < 
 |_| |_|\__,_|___/_| |_|      \___|_|  \__,_|\___|_|\_\
                                        github:swipax
                                                       
        """)
banner()
class Slow:
    @classmethod
    def slowType(cls, text: str, speed: float, color=None, newLine=True):
        for i in text:
            print((color or "") + i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()
        

def crack_md5_hash(hash, password_list_path):
    with open(password_list_path, "r") as f:
        for password in f.readlines():
            password = password.strip()
            if hashlib.md5(password.encode()).hexdigest() == hash:
                return password
  

def crack_sha256_hash(hash, password_list_path):
    with open(password_list_path, "r") as f:
        for password in f.readlines():
            password = password.strip()
            if hashlib.sha256(password.encode()).hexdigest() == hash:
                return password
    

def crack_sha512_hash(hash, password_list_path):
    with open(password_list_path, "r") as f:
        for password in f.readlines():
            password = password.strip()
            if hashlib.sha512(password.encode()).hexdigest() == hash:
                return password
    

def crack_sha1_hash(hash, password_list_path):
    with open(password_list_path, "r") as f:
        for password in f.readlines():
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
 

def crack_password(hash, password_list_path):
    password = crack_md5_hash(hash, password_list_path)
    if password:
        return password
    password = crack_sha256_hash(hash, password_list_path)
    if password:
        return password
    password = crack_sha512_hash(hash, password_list_path)
    if password:
        return password
    password = crack_sha1_hash(hash, password_list_path)
    if password:
        return password
   


password_hash = input(Fore.BLUE + "HASH: " + Style.NORMAL)
password_list_path = input(Fore.CYAN + "Password File Path: "+ Style.NORMAL )

cracked_password = crack_password(password_hash, password_list_path)
if cracked_password:
    print()
    Slow.slowType(f"Cracked Hash: {cracked_password}",0.1,color=Fore.GREEN,newLine=True)
else:
    print()
    Slow.slowType("Hash not cracked.",0.1,color=Fore.RED,newLine=True)
