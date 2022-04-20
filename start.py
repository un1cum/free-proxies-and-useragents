"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                             Free proxies and user agents                        ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║                                                     
║                                                                                 ║
║  The authors of this program are not responsible for its use!                   ║
║  When placing this code on third-party resources, please indicate the authors!  ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2022 ebankoff                           ║
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
import ctypes
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
	param=input(Fore.WHITE + '\nExit? yes/no: ')
	if param == 'yes':
		if platform == 'win32':
			os.system("cls")

		else:
			os.system("clear")
		print(
			'     I would be grateful if you star on this repository on GitHub:',
			'\n          https://github.com/ebankoff/free_proxies_useragents',
			'\n',
			'\n          You can support me by sending any amount to my Qiwi:',
			'\n                        qiwi.com/n/HERAMANT',
			'\n',
			'\n                    Copyright (C) 2022 ebankoff')
		print("\nPress Enter to exit")
		input()
		os.abort()
	elif param == 'no':
		if platform == 'win32':
			os.system("cls")
		else:
			os.system("clear")
		main()

	else:
		print(Fore.RED + '\n━━━━━━━━━━ERROR━━━━━━━━━━\n')
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

	print(Fore.RED + '█▀▀ █▀█ █▀▀ █▀▀   █▀█ █▀█ █▀█ ▀▄▀ █ █▀▀ █▀   ▄▀█ █▄ █ █▀▄   █ █ █▀ █▀▀ █▀█ ▄▀█ █▀▀ █▀▀ █▄ █ ▀█▀ █▀',
		Fore.WHITE + '\n█▀  █▀▄ ██▄ ██▄   █▀▀ █▀▄ █▄█ █ █ █ ██▄ ▄█   █▀█ █ ▀█ █▄▀   █▄█ ▄█ ██▄ █▀▄ █▀█ █▄█ ██▄ █ ▀█  █  ▄█\n')

	print(Fore.RED + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print(Fore.WHITE + " Created by ebankoff - https://github.com/ebankoff")
	print(Fore.WHITE + " There could have been your ad here")
	print(Fore.RED + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

	print(
		Fore.RED + '\n[' + Fore.WHITE + '0' + Fore.RED + ']' + Fore.WHITE + ' Exit',
		Fore.RED + '\n[' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.WHITE + ' Search proxies',
		Fore.RED + '\n[' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.WHITE + ' Search user agents',
		Fore.RED + '\n[' + Fore.WHITE + '3' + Fore.RED + ']' + Fore.WHITE + ' Print saved proxies',
		Fore.RED + '\n[' + Fore.WHITE + '4' + Fore.RED + ']' + Fore.WHITE + ' Print saved user agents',
		Fore.RED + '\n[' + Fore.WHITE + '5' + Fore.RED + ']' + Fore.WHITE + ' Delete saved proxies',
		Fore.RED + '\n[' + Fore.WHITE + '6' + Fore.RED + ']' + Fore.WHITE + ' Delete saved user agents'
		)
	try:
		ans = int(input('\n → '))
		if ans == 0:
			ex()

		elif ans== 1:
			res = requests.get('https://hidemy.name/ru/proxy-list', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
			soup = BeautifulSoup(res.text,"lxml")
			
			with open(r"proxies.txt", "a", encoding="utf-8") as file:
				for child in soup.recursiveChildGenerator():
					if child.name=='td':
						if validate_ip(child.text):
							file.write(child.text)
							file.write(':')
						if validate_port(child.text):
							file.write(child.text)
							file.write('\n')

			res2 = requests.get('https://free-proxy-list.net', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
			soup2 = BeautifulSoup(res2.text,"lxml")

			cnt2=0

			with open(r"proxies.txt", "a", encoding="utf-8") as file:
				for child in soup2.recursiveChildGenerator():    
					if child.name=='td':
						if cnt2 == 0:
							if not validate_ip(child.text):
								break
							file.write(child.text)
							file.write(':')
						if cnt2 == 1:
							file.write(child.text)
							file.write('\n')

						cnt2 = (cnt2 + 1) % 8
			print(Fore.WHITE + "\nSuccess! File: proxies.txt")
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

			with open(r"useragents.txt", "a") as file:
				file.write(ans3[:-4])
				file.write('\n')

			print(Fore.WHITE + "\nSuccess! File: useragents.txt")
			ex()

		elif ans == 3:
			print("")
			cnt = 1
			with open(r"proxies.txt", "r") as file:
				for line in file:
					line = line.replace('\n', '')
					print(Fore.RED + '[' + Fore.WHITE + str(cnt) + Fore.RED + '] ' + Fore.WHITE + line)
					cnt += 1
				ex()

		elif ans == 4:
			print("")
			cnt = 1
			with open(r"useragents.txt", "r") as file:
				for line in file:
					line = line.replace('\n', '')
					print(Fore.RED + '[' + Fore.WHITE + str(cnt) + Fore.RED + '] ' + Fore.WHITE + line)
					cnt += 1
				ex()

		elif ans == 5:
			os.remove('proxies.txt')

		elif ans == 6:
			os.remove('useragents.txt')

		else:
			print(Fore.RED + '\n━━━━━━━━━━ERROR━━━━━━━━━━\n')
			ex()

	except:
		print(Fore.RED + '\n━━━━━━━━━━ERROR━━━━━━━━━━\n')
		ex()

if __name__=='__main__':
	if platform == 'win32':
		ctypes.windll.kernel32.SetConsoleTitleW("free proxies and useragents")
	main()