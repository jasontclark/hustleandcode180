#!/usr/bin/env python
""" load_balancer.py - simulated load balancer """
import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]
# SERVERS = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7']

# n = -1
# def get_server():
#     global n
#     n += 1
#     print SERVERS[n % len(SERVERS)]

# import itertools
# cycle = itertools.cycle(SERVERS)
# def get_server():
#     global cycle
#     return cycle.next

# def get_server()
#     try:
#         return next(get_server.s)
#     except StopIteration;
#         get_server.s = iter(SERVERS)
#         return next(get_server.s)
# setattr(get_server, 's', iter(SERVERS))

def get_server():
    def f():
        while True:
            i = SERVERS.pop(0)
            SERVERS.append(i)
            yield i
    return next(f())

if __name__ == '__main__':
    from random import randint
    for i in range(10):
        a = randint(5,99)
        b = randint(5,99)

        server = get_server()

        print server.print_name()
        print server.multiply_handler(a,b)
        print server.last_multiplied_handler()
        print ' '
