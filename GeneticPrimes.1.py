from __future__ import division
import random, sys, os, tempfile, subprocess

generation = 1

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
quadsVars=[1,2,3]
quads=[0] * generation

fileName=os.path.basename(__file__)

if (generation>1):
    ID0=fileName.split(".")
    ID0=ID0[1:-2]
    ID0[0]=str(int(ID0[0])-1)

    quadReference="Quads."+".".join(ID0)+".txt"
    print quadReference
    storePath="/Users/jadtayl/Desktop/Programming/Genetic-Primes/Quadratic Storage/"+quadReference
    storeEx=open(storePath)

#quads[generation-1]=
def primeChecker(n):
    n=abs(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(1,generation+1):
    lgb=i*100
    smb=(i-1)*100
    for x in range(smb,lgb):
        gen[x-1]=(x*x)-x+41
        #sub[x-1]=quads[i](x)

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
    newtext=newtext[:91]+newgen+newtext[92:]

    store="/Users/jadtayl/Desktop/Programming/Genetic-Primes/Quadratic Storage/Quads"+fileName[13:-3]+".txt"
    quadStorage = open(store, "w")
    quadStorage.write(str(quadsVars))
    quadStorage.close()


    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    for x in xrange(int(functValue*100)):
        identity=str(x+1)
        name=dirpath+fileName[:14]+newgen+fileName[15:-2]+identity+".py"

        newFunction=open(name,"w")
        newFunction.write(newtext)
        newFunction.close()
        #subprocess.Popen(["python", name])
cloneFunction()
print functValue
