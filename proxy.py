import os
import re
import emoji
import sys
import time
import urllib
import socket
import bs4
import requests
import json
import colorama
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from colorama import Fore, Back
from unicodedata import normalize
from urllib.request import urlopen as uReq

colorama.init()

def logo():
	print(Fore.YELLOW + """
╔══╦═╦══╦╗╔╦╗ ╔╗ ╔══╦══╦═╦══╦══╦══╦═╗
║╔╗║╔╣╔╗╠╬╬╣║ ║║ ║══╣╔═╣╔╣╔╗║╔╗║ ═╣╔╝
║╚╝║║║╚╝╠╬╬╣╚═╝║ ╠══║╚═╣║║╔╗║╚╝║ ═╣║
║╔═╩╝╚══╩╝╚╩═╗╔╝ ╚══╩══╩╝╚╝╚╣╔═╩══╩╝
║║         ╔═╝║             ║║
╚╝         ╚══╝             ╚╝""")

def ex():
	param=input('Exit? yes/no: ')
	if param == 'yes':
		exit(0)
	elif param == 'no':
		main()
	else:
		print('ERROR: invalid value')
		ex()

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

def pb():
	toolbar_width = 40
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) 

	for i in range(toolbar_width):
	    time.sleep(0.1) 
	    sys.stdout.write("█")
	    sys.stdout.flush()

	sys.stdout.write("]\n") 

def main():
	res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
	soup = BeautifulSoup(res.text,"lxml")

	cnt=0
	ip=16
	port=6
	ct=20

	print("""
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃1) Search proxy            ┃
┃2) Saved proxy             ┃
┃3) Delete saved proxy      ┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
		""")
	ans=input(">> ")
	if(ans=='1'):
		with open(r"proxy.txt", "a") as file:
			for child in soup.recursiveChildGenerator():    
			    if child.name=='td':
			        if cnt == 0:
			            if not valid_ip(child.text):
			                break
			            file.write(str("IP: " + child.text))
			            spaces = ip-len(child.text)
			            file.write(' ' * spaces + '| ')
			        if cnt == 1:
			            file.write(str("PORT: " + child.text))
			            spaces = port-len(child.text)
			            file.write(' ' * spaces + '| ')
			        if cnt == 3:
			            file.write(str("COUNTRY: " + child.text))
			            spaces = ct-len(child.text)
			            file.write(' ' * spaces + '| ')
			        if cnt == 4:
			            file.write(str("TYPE: " + child.text + '\n'))
			        cnt = (cnt + 1) % 8
		pb()
		print("Success! Proxy file: proxy.txt")
		ex()

	elif(ans=='2'):
		with open(r"proxy.txt", "r") as file:
		    for line in file:
		        print(line)
		    ex()

	elif(ans=='3'):
		os.remove('proxy.txt')

	else:
		print("ERROR: invalid value")
		ex()

if __name__=='__main__':
	logo()
	main()