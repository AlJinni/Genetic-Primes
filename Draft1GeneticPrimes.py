from __future__ import division
import os
import subprocess
import tempfile
import random
import sys
import itertools

generation = 1

squcos=[]
squcog=[]
lincos=[]
lincog=[]
varcos=[]
varcog=[]
gen=[]
sub=[]

for i in xrange(generation):
    squcos.append(1)
    lincos.append(1)
    varcos.append(1)

for i in range(0,100):
    gen.append(0)
    sub.append(0)

for i in xrange(generation):
    squcos[i]=random.randint(-100,100)
    lincos[i]=random.randint(-100,100)
    varcos[i]=random.randint(-100,100)

for i in xrange(generation):
    for x in range(0,100):
        gen[x-1]=(x*x)-x+41
        sub[x-1]=squcos[i]*x*x+lincos[i]*x+varcos[i]

gen.sort()
genlength=len(gen)-1
sublength=len(sub)-1
for i in sub:
    sub[sub.index(i)]=abs(i)
for i in gen:
    gen[gen.index(i)]=abs(i)

sub.sort()
for x in xrange(sublength):
    if (sub[x]>gen[genlength]):
        for i in range(x,sublength):
            sub.pop(i)
            break
        break
sublength=len(sub)-1

datalist = []

def primeChecker(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for x in sub:
    if primeChecker(x):
        for i in gen:
            if (i==x):
                gen.pop(gen.index(i))
                sys.exit()

for x in sub:
    for i in gen:
        if (x==i):
            gen.pop(gen.index(i))
primes=list(gen)

for j in primes:
    if not primeChecker(j):
        primes.pop(primes.index(j))
lenprimes=len(primes)
lengen=len(gen)
functValue=lenprimes/lengen
print functValue
