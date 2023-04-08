#!/bin/python3

import sys

def primeQ(p):
    if p == 2:
        return True
    if p% 2 ==0 :
        return False
    i =3
    while i**2 <= p:
        if p%i ==0:
            return False
        i += 2
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    for i in range(1,n+1):
        if n%i == 0 :
            if primeQ(n//i):
                print(n//i)
                break