open('loggef.so','w')
open('loggef32.so','w')

try:
  from concurrent.futures import ThreadPoolExecutor
  import os,sys,time,random,hashlib
  from uuid import getnode
  import platform
  import mysql.connector
  import requests,json
  from termcolor import colored
  from colorama import Fore,Back,Style
  from bs4 import BeautifulSoup as bs
  from datetime import datetime
except:
  print('Run setup.py first')
  sys.exit()


i='\033[1;32;40m|\033[1;0m'
ii='\033[1;31;40m[\033[1;0m'
iii='\033[1;31;40m]\033[1;0m'
pi='\033[1;32;40m+\033[1;0m'




os.system('clear')

dd=random.choice('4 3 2 1'.split())
def banner():
    os.system('clear')
    global ban
    ban=colored(f'''
         ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
                   \033[1;36;40m╔═🅲🅾🅳🅴🅳 🅱🆈 🅹🅾🆂🅸🅵━━╗     
  \033[1;3{dd};40m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
. ######৳৳৳৳৳৳Fuck###########
  \033[1;0m''','red',attrs=['bold'])
    ner=f'''
  \033[1;31;40m╔═════════════════════════════════════════════════════╗
  ╣\033[1;3{dd};40m  ╭─────────────────────────────────╮ ═══════════════\033[1;31;40m╠
  ╣\033[1;3{dd};40m══ Aᴜᴛʜᴏʀ : Mᴅ Jᴏꜱɪғ Kʜᴀɴ              ══════════════\033[1;31;40m╠
  ╣\033[1;3{dd};40m══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═══════════════\033[1;31;40m╠
  \033[1;31;40m╚═════════════════════════════════════════════════════╝\n'''



    Banner=ban+ner
    print(Banner)

message=f"""
  \033[1;32;40m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  \033[1;3{dd};40m│  THIS TOOL IS UPDATING, YOU CANNOT USE IT NOW'      │
  \033[1;3{dd};40m│       IF YOU HAVE ANY QUESTION, CONTACT LINK        │
  \033[1;3{dd};40m│               facebook.com/josifvai                 │
  \033[1;3{dd};40m│                                                     │
  \033[1;32;40m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""


def main():
  banner()
  print(message)
  input()
  sys.exit()
main()
