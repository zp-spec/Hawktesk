from os import *
from time import sleep
from datetime import datetime
true = True
false = False
#osfile
system("cd HAWK")
#os
os = input("root@loccalhost: ")
if os == "git clone":
	o = input("Clone: ")
	if o == (o):
		system(f"git clone {o}")
		system("python hawklinux.py")
if os == "ls":
	system("ls")
	system("python hawklinux.py")

if os == "cd":
	k = input("file name: ")
	if k == (k):
		system(f"cd {k}")
		system("python hawklinux.py")
if os == "aap install *":
	system("pkg install * &>> hawkaap.log")
if os == "pip install *":
	system("pip install * &>> hawkpip.log")
else:
	print(f"command {os} is not found")
	system("python hawklinux.py")