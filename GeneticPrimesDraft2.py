from __future__ import division
import random, sys, os, tempfile

generation = 1

s0=[]
l0=[]
c0=[]
gen=[]
sub=[]

def primeChecker(n):
    n=abs(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in xrange(generation+1):
    s0.append(random.randint(-100,100))
    l0.append(random.randint(-100,100))
    c0.append(random.randint(-100,100))

for i in range(1,100*generation+1):
    gen.append(0)
    sub.append(0)

for i in range(1,generation+1):
    lgb=i*100
    smb=(i-1)*100
    for x in range(smb,lgb):
        gen[x-1]=(x*x)-x+41
        sub[x-1]=s0[i]*x*x+l0[i]*x+c0[i]

genlength=len(gen)-1
sublength=len(sub)-1

for x in sub:
    for i in gen:
        if (i==x):
            if primeChecker(x):
                print x
                print "FAILED"
                sys.exit()
            gen.remove(i)

primes=list(gen)

for j in primes:
    if not primeChecker(j):
        primes.remove(j)

functValue=len(primes)/len(gen)

newtext=open(__file__,"r").read()
newgen=str(generation+1)
dirpath = "/Users/jadtayl/Desktop/Programming/Genetic-Primes/Prime Functions/Gen "+newgen
newtext=newtext[:79]+newgen+newtext[80:]
if not os.path.exists(dirpath):
    os.makedirs(dirpath)
for x in xrange(int(functValue*100)):
    newFunction=tempfile.NamedTemporaryFile("w", suffix=newgen+".py", dir=dirpath, delete=False)
    newFunction.write(newtext)
    newFunction.close()

print functValue
