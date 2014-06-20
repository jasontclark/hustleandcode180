#!/usr/bin/env python
""" load_balancer.py - simulated load balancer """
SERVERS = ['APP1', 'APP2', 'APP3']

n = -1

def get_server():
    global n
    n += 1
    print SERVERS[n % len(SERVERS)]


num = 10

for i in num:
    get_server
    i -= 1
