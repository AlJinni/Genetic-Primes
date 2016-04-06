from __future__ import division
import random, sys, os, tempfile, subprocess

generation = 1

import time

class Quadratic:
    def __init__(self, square, linear, constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d, %d, %d)" % (self.square, self.linear, self.constant)

gen=[0]*100*generation
sub=[0]*100*generation
quadsVars=[]
quads=[0] * generation

fileName=os.path.abspath(__file__)

if (generation>1):
    ID0=fileName.split(".")
    ID0=ID0[1:-2]
    ID0[0]=str(int(ID0[0])-1)

    quadReference="Quads."+".".join(ID0)+".txt"
    storePath="/Users/jadtayl/Desktop/Programming/Genetic-Primes/Quadratic Storage/"+quadReference
    with open(storePath) as storeEx:
        quadsVars=storeEx.read()
    quadsVars=quadsVars.strip("[").strip("]").replace(" ",'')
    quadsVars=quadsVars.split(",")

for x in quadsVars:
    quadsVars[quadsVars.index(x)]=int(x)
while len(quadsVars) < (generation*3):
    quadsVars.append(random.randint(0,100))
for x in xrange(generation):
    quads[x]=Quadratic(quadsVars[x],quadsVars[x+1],quadsVars[x+2])

def primeChecker(n):
    n=abs(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in xrange(1,generation+1):
    lgb=i*100
    smb=(i-1)*100
    for x in range(smb,lgb):
        gen[x-1]=(x*x)+x+41
        sub[x-1]=quads[i-1](x)

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

def cloneFunction():
    newtext=open(__file__,"r").read()
    newgen=str(generation+1)
    dirpath = "/Users/jadtayl/Desktop/Programming/Genetic-Primes/PrimeFunctions/Gen "+newgen+"/"
    newtext=newtext[:91]+newgen+newtext[newtext.find('\n',91):]

    store="/Users/jadtayl/Desktop/Programming/Genetic-Primes/Quadratic Storage/Quads"+fileName[13:-3]+".txt"
    quadStorage = open(store, "w")
    quadStorage.write(str(quadsVars))
    quadStorage.close()

    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    for x in xrange(int(functValue*100)):
        identity=str(x+1)
        name=dirpath+fileName[:14]+newgen+fileName[fileName.find('.',14):-2]+identity+".py"
        newFunction=open(name,"w")
        newFunction.write(newtext)
        newFunction.close()
        subprocess.Popen(["python", name])

        time.sleep(100)

if generation<15:
    cloneFunction()
else:
    dataPath = "/Users/jadtayl/Desktop/Programming/Genetic-Primes/PrimeFunctions/Data/"
    if not os.path.exists(dataPath):
        os.makedirs(dataPath)
    dataFile = dataPath+"Functionality="+str(functValue)+" Identity="+fileName[14:-3]+".txt"
    dataStore = open(dataFile, "w")
    dataStore.write("Identifier: "+fileName[14:-3]+"\n\nQuadratic Coefficients: "+str(quadsVars)+"\n\nFunctionality Value: "+str(functValue))
    sys.exit()
