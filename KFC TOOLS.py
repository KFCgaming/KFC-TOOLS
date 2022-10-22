from asyncore import write
from multiprocessing.connection import wait
from platform import win32_edition
from pystyle import Center
from pystyle import Anime, Colors, Colorate, System, Center, Write
from colorama import Fore
from colorama import Style
import os
import time
import requests
import sys
import urllib.request
import random

os.system("title KFC Tool's")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"

ytb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"

char = "1234567890"

discordinvchar = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopmlkjhgfdsqwxcvbn123456789"

nitrolist = ["https://bit.ly/3uTw3UC",
"https://bit.ly/3T8CrEo",
"https://bit.ly/RobuxFree_2022",
"http://alturl.com/p749b"]

num = random.randint(3, 25)

discordinvnum = random.randint(5, 10)

def gtproxy():
  req = urllib.request.Request("http://free-proxy-list.net/")
  req.add_header(
    "User-Agent",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
  sourcecode = urllib.request.urlopen(req)
  part = str(sourcecode.read())
  part = part.split("<tbody>")
  part = part[1].split("</tbody>")
  part = part[0].split("<tr><td>")
  proxylist = ""
  for proxy in part:
    proxy = proxy.split("</td><td>")
    try:
      proxylist = proxylist + proxy[0] + ":" + proxy[1] + "\n"
    except:
      pass
  out_file = open("proxy.txt", "w")
  out_file.write(proxylist)
  out_file.close()
  print()
  Write.Print("•----------•\n", Colors.red_to_blue, interval=0.1000)
  Write.Print("The proxies are in proxy.txt", Colors.red_to_blue, interval=0.0025)
  Write.Input("", Colors.red_to_blue, interval=0.0025)

def tkgen():

    print()
    Write.Print("•----------•\n", Colors.red_to_blue, interval=0.1000)
    Write.Print("The tokens are in tokens.txt", Colors.red_to_blue, interval=0.0025)
    Write.Print("\n \n Close the program to stop the generator", Colors.red_to_blue, interval=0.0025)


    for i in range (9999999999999999999999999999999999):
     first = '' .join((random.choice(chars) for i in range (16))) 
     second = ''.join((random.choice(chars) for i in range(6))) 
     third = ''.join((random.choice(chars) for i in range (27)))

     result = "OTk3NDE0" + first + "." + second + "." + third

     output = open("tokens.txt", "a") 
     output.write(result + "\n")

    Write.Input("", Colors.red_to_blue, interval=0.0025)

def ipgen():

    print()
    Write.Print("•----------•\n", Colors.red_to_blue, interval=0.1000)
    Write.Print("The IP Adress are in IPAdress.txt", Colors.red_to_blue, interval=0.0025)
    Write.Print("\n \n Close the program to stop the generator", Colors.red_to_blue, interval=0.0025)

    for i in range (9999999999999999999999999999999999999):
     first = '' .join((random.choice(char) for i in range (3))) 
     second = ''.join((random.choice(char) for i in range (2))) 
     third = ''.join((random.choice(char) for i in range (2))) 
     four = ''.join((random.choice(char) for i in range (2))) 

     result = first + "." + second + "." + third + "." + four

     output = open("IPAdress.txt", "a") 
     output.write(result + "\n")

    Write.Input("", Colors.red_to_blue, interval=0.0025)

def discordserver():
    print()
    Write.Print("Discord Server : https://discord.gg/28W5rnANSW", Colors.red_to_blue,interval=0.0025)
    Write.Input("", Colors.red_to_blue, interval=0.0025)

def rytbvideo():
    for i in range (1000):
     urlytb = '' .join((random.choice(ytb) for i in range (11))) 

     result = "https://www.youtube.com/watch?v=" + urlytb

     print()
     Write.Print(result, Colors.red, interval=0.0025)
     Write.Input("", Colors.red_to_blue, interval=0.0025)

def rdiscordinv():
    for i in range (1000):
     discordinv = '' .join((random.choice(discordinvchar) for i in range (discordinvnum))) 

     result = "https://discord.gg/" + discordinv

     print()
     Write.Print(result, Colors.blue, interval=0.0025)
     Write.Input("", Colors.red_to_blue, interval=0.0025)

def nitrofree():

    print()
    Write.Print("•----------•    \n", Colors.red_to_blue, interval=0.1000)
    Write.Print(random.choice(nitrolist), Colors.red_to_blue, interval=0.0025)
    Write.Input("", Colors.red_to_blue, interval=0.0025)

def rbitly():
    for i in range (1000):
     urlytb = '' .join((random.choice(ytb) for i in range (num))) 

     result = "https://bit.ly/" + urlytb

     print()
     Write.Print(result, Colors.red, interval=0.0025)
     Write.Input("", Colors.red_to_blue, interval=0.0025)

def activatewin():
  Write.Print("Click Here to Install ActivateWindows.bat\n", Colors.red_to_blue, interval=0.005)
  Write.Print("https://bit.ly/3T1Y3T2", Colors.red_to_blue, interval=0.005)
  Write.Input("", Colors.red_to_blue, interval=0.0025)
  

print()
print(
  Center.XCenter(
    Colorate.Horizontal(
      Colors.red_to_blue,  """

  ██╗░░██╗███████╗░█████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗ V0.2
  ██║░██╔╝██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝ Made by KFCgamingFR
  █████═╝░█████╗░░██║░░╚═╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
  ██╔═██╗░██╔══╝░░██║░░██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
  ██║░╚██╗██║░░░░░╚█████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝ 
  ╚═╝░░╚═╝╚═╝░░░░░░╚════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
""", 1)))
print(
    Center.XCenter(
        Colorate.Horizontal(
            Colors.blue_to_red, """
 ╔═══════════════════════════════════════════════════════════════════╗
 ║                                                                   ║
 ║                            GENERATOR                              ║
 ║                                                                   ║
 ║                 1. IP Adress   2. Discord Token                   ║
 ║                                                                   ║
 ║                             RANDOM                                ║
 ║                                                                   ║
 ║        3. Random Youtube Video     4. Random Discord Invite       ║
 ║                      5. Random Bit.ly Link                        ║
 ║                                                                   ║
 ║                              FREE                                 ║
 ║                                                                   ║
 ║                6. Free Nitro     7. Activate Windows              ║
 ║                         8. Get Proxy                              ║
 ║                                                                   ║
 ║                       9.Discord Server                            ║
 ║                                                                   ║
 ╚═══════════════════════════════════════════════════════════════════╝
""", 1)))
print()
choice = Write.Input("Choice your APP   ", Colors.red_to_blue, interval=0.0025)

if choice == "1":
  ipgen()
if choice == "2":
  tkgen()
if choice == "8":
  gtproxy()
if choice == "3":
  rytbvideo()
if choice == "4":
  rdiscordinv()
if choice == "9":
  discordserver()
if choice == "6":
  nitrofree()
if choice == "5":
  rbitly()
if choice == "7":
  activatewin()

else:
  exit()