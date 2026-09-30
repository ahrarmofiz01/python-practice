import time
import random
import os

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

clear()

type_text(GREEN + ">>> HACKING NASA..." + RESET)
time.sleep(1)

type_text(YELLOW + ">>> Bypassing firewall..." + RESET)
time.sleep(1)

type_text(GREEN + ">>> Downloading secret files..." + RESET)
time.sleep(1)

for i in range(5):
    print(GREEN + f">>> Downloading... {random.randint(1,99)}%" + RESET)
    time.sleep(0.3)

type_text(RED + ">>> ACCESS DENIED 💀" + RESET)
time.sleep(1)

type_text(YELLOW + ">>> Trying another method..." + RESET)
time.sleep(1)

type_text(GREEN + ">>> Asking Google for password..." + RESET)
time.sleep(1)

type_text(RED + ">>> Password: 123456" + RESET)
time.sleep(1)

type_text(GREEN + ">>> ACCESS GRANTED 😂" + RESET)

time.sleep(2)

print()
print(GREEN + r"""
      ██████╗ ██╗  ██╗
      ██╔══██╗██║  ██║
      ██████╔╝███████║
      ██╔═══╝ ██╔══██║
      ██║     ██║  ██║
      ╚═╝     ╚═╝  ╚═╝
""" + RESET)

print(YELLOW + "        BRO IS A HACKER 💀" + RESET)
