"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                      Scraper                                    ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║                                                     
║                                                                                 ║
║  The authors of this program are not responsible for its use!                   ║
║  When placing this code on third-party resources, please indicate the authors!  ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2021 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import re
import bs4
import sys
import time
import json
import urllib
import socket
import requests
import colorama
import numpy as np
import pandas as pd
from sys import platform
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import urlopen as uReq
from colorama import Fore, Back, Style, init

colorama.init()

if platform == 'win32':
	os.system("cls")

else:
	os.system("clear")

def ex():
	param=input(Fore.YELLOW + 'Exit? yes/no: ')
	if param == 'yes':
		if platform == 'win32':
			os.system("cls")

		else:
			os.system("clear")
		print('''\033[36m
																		 
                         Thanks for using scraper!
        I would be grateful if you star on this repository on GitHub:
                    https://github.com/ebankoff/scraper

            You can support me by sending any amount to my Qiwi:
                            qiwi.com/n/HERAMANT

                       Copyright (C) 2021 ebankoff                                                                            
			''')
		print("Press Enter to exit")
		input()
		exit()
	elif param == 'no':
		if platform == 'win32':
			os.system("cls")

		else:
			os.system("clear")
		main()

	else:
		print(Fore.RED + 'ERROR: invalid value')
		ex()

def validate_ip(ip):
	a = ip.split('.')
	if len(a) != 4:
		return False
	for x in a:
		if not x.isdigit():
			return False
		i = int(x)
		if i < 0 or i > 255:
			return False
	return True

def validate_port(port):
	try:
		if int(port)>=1 and int(port)<=65535:
			return True
		else:
			return False
	except:
		return False

def main():
	res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
	soup = BeautifulSoup(res.text,"lxml")

	cnt=0
	ip=16
	port=6
	ct=20

	print(Fore.YELLOW + Style.BRIGHT + """╭━━━╮
┃╭━╮┃
┃╰━━┳━━┳━┳━━┳━━┳━━┳━╮
╰━━╮┃╭━┫╭┫╭╮┃╭╮┃ ━┫╭╯
┃╰━╯┃╰━┫┃┃╭╮┃╰╯┃ ━┫┃
╰━━━┻━━┻╯╰╯╰┫╭━┻━━┻╯
            ┃┃
            ╰╯""")

	print("\033[0m" + Fore.CYAN + "================================================")
	print(Fore.YELLOW + "Created by Eban'ko - https://github.com/ebankoff")
	print(Fore.YELLOW + "       There could have been your ad here")
	print(Fore.CYAN + "================================================")

	print("""
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m0\033[0m\033[40m\033[35m]\033[31m Exit                    \033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m4\033[0m\033[40m\033[35m] Print saved user agents
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m1\033[0m\033[40m\033[35m] Search proxies          \033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m5\033[0m\033[40m\033[35m] Delete saved proxies
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m2\033[0m\033[40m\033[35m] Search user agents      \033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m6\033[0m\033[40m\033[35m] Delete saved user agents
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m3\033[0m\033[40m\033[35m] Print saved proxies
		""")
	try:
		ans = int(input('\033[0m\033[40m\033[35m → \033[32m'))
		if ans == 0:
			ex()

		elif ans== 1:
			res = requests.get('https://hidemy.name/ru/proxy-list', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
			soup = BeautifulSoup(res.text,"lxml")
			
			with open(r"proxy.txt", "a", encoding="utf-8") as file:
				for child in soup.recursiveChildGenerator():
					if child.name=='td':
						if validate_ip(child.text):
							file.write(str("IP: " + child.text))
							spaces = ip-len(child.text)
							file.write(' ' * spaces + '| ')
						if validate_port(child.text):
							file.write(str("PORT: " + child.text))
							spaces = port-len(child.text)
							file.write(' ' * spaces + '\n')

			res2 = requests.get('https://free-proxy-list.net', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
			soup2 = BeautifulSoup(res2.text,"lxml")

			cnt2=0

			with open(r"proxy.txt", "a", encoding="utf-8") as file:
				for child in soup2.recursiveChildGenerator():    
					if child.name=='td':
						if cnt2 == 0:
							if not validate_ip(child.text):
								break
							file.write(str("IP: " + child.text))
							spaces = ip-len(child.text)
							file.write(' ' * spaces + '| ')
						if cnt2 == 1:
							file.write(str("PORT: " + child.text))
							spaces = port-len(child.text)
							file.write(' ' * spaces + '\n')

						cnt2 = (cnt2 + 1) % 8
			print(Fore.CYAN + "Success! Proxy file: proxy.txt")
			ex()

		elif ans == 2:
			res = requests.get('https://useragents.ru/stable.html', headers={'User-Agent':'Mozilla/5.0'})
			soup = BeautifulSoup(res.text,"lxml")

			ans = soup.find("span", {"style": "color:#000000;font-family:Arial;font-size:13px;"})
			ans2=str(ans)
			ans3=""
			ans4=""

			for i in range(61, len(ans2)-1):
				if(ans2[i]!='<' and ans2[i]!='>' and ans2[i]+ans2[i+1]!='br' and ans2[i]!='r' and ans2[i]!='/'):
					ans3+=ans2[i]
				if(ans2[i]=='"' or ans2[i]+ans2[i+1]=='br'):
					ans3+='\n'

			with open(r"user.txt", "a") as file:
				file.write(ans3[:-4])
				file.write('\n')

			print(Fore.CYAN + "Success! User Agent file: user.txt")
			ex()

		elif ans == 3:
			print("")
			with open(r"proxy.txt", "r") as file:
				for line in file:
					print(Fore.CYAN + line)
				ex()

		elif ans == 4:
			print("")
			with open(r"user.txt", "r") as file:
				for line in file:
					print(Fore.CYAN + line)
				ex()

		elif ans == 5:
			os.remove('proxy.txt')

		elif ans == 6:
			os.remove('user.txt')

		else:
			print(Fore.RED + "ERROR: invalid value")
			ex()

	except:
		print(Fore.RED + "ERROR: invalid value")
		ex()

if __name__=='__main__':
	main()
