from __future__ import division
import sys, os, tempfile, subprocess, numpy

generation=1

import time
from random import randint
from fractions import gcd

fileName=os.path.basename(__file__)

#Call complete program with metaKlaubber(limit)

#Indexes at ZERO: Limit 0<=n<infinity: A function that will return the value of q for a given n (see "prime stuffs" google document)

qFunction=[]

#http://stackoverflow.com/questions/27878137/how-to-check-if-the-number-can-be-represented-prime-power-nth-root-is-prime-or
def findWitness(n, k=5): # miller-rabin
    s = 0
    d = n-1
    while d % 2 == 0:
        s = s+1
        d=d/2
    for i in xrange(k):
        a = randint(2, n-1)
        x = pow(a, int(d), n)
        if x == 1 or x == n-1: continue
        for r in xrange(s-1):
            x = (x * x) % n
            if x == 1: return a
            if x == n-1: break
        else: return a
    return 0

# returns p,k such that n=p**k, or 0,0
# assumes n is an integer greater than 1

def primePower(n):
    def checkP(n, p):
        k = 0
        while n > 1 and n % p == 0:
            n, k = n / p, k + 1
        if n == 1: return p, k
        else: return False
    if n % 2 == 0: return checkP(n, 2)
    q = n
    while True:
        a = findWitness(q)
        if a == 0: return checkP(n, q)
        d = gcd(pow(a,q,n)-a, q)
        if d == 1 or d == q: return False
        q = d

def q(r):
    n=2
    while len(qFunction)<r:
        if not primePower(n):
            qFunction.append(n)
        n=n+1
    return qFunction[r-1]

#Indexes at ONE: Limit 0<n<infinity: A function that will return the value of d for a given n (see "prime stuffs" google document)
def d(n):
    if (n==1):
        return 5

    if (n==2):
        return 9

    else:
        if (n%2==0):
            return 13 + 2*(n-4)

        if (n%2==1):
            return 7 + 2*(n-3)


def fMeta(maxEx):
    fMetaRay = []
    if (maxEx<245):
        return fMetaRay
    initValue = 0
    n=0
    while initValue<maxEx:
        n=n+1
        Q = q(n)
        D = d(n)
        initValue = Q - (Q+D) + Q*41 - n + d(n)
        latestValue = 0
        floorN = numpy.floor((n/2)+1)
        i = 0
        while 1 == 1:
            i=i+1
            if(latestValue<maxEx):
                fMetaRay.append(int(Q*i*i - (Q+D)*i + Q*41 - floorN + d(n)))
                fMetaRay.append(int(Q*i*i - (Q-D)*i + Q*41 - floorN))
                latestValue = int(Q*i*i - (Q-D)*i + Q*41 - floorN)

            else:
                break
    return fMetaRay

#Primality test, but accepts 1 as a prime number
def isPrime(x):
    for i in range(2,1+int(numpy.sqrt(x))):
        if x%i == 0:
           return False
    return True


class Quadratic:
    def __init__(self, square,linear,constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d,%d,%d)" % (self.square,self.linear,self.constant)

def klaubberNumArray(r):
    result = []
    k = Quadratic(1, -1, 41)
    for i in range(0,r):
        result.append(k(i))
    return result

def meta(n, rang):
    k = Quadratic(1, -1, 41)
    metaRay = []
    if n==1:
        i = 0
        while True:
            metaVar = i * i + 41
            if (metaVar > rang):
                break
            metaRay.append(metaVar)
            i = i + 1
    elif n==2:
        j = 1
        while True:
            metaVar = ((j * (j - 1)) / 2) + 82
            if metaVar > rang:
                break
            metaRay.append(metaVar)
            j = j + 1
    else:
        m = 2 * (n-1)
        metaVarOdd = 1
        metaVarFact = m
        prevNum = 41 * n
        k = 0
        while True:
            if prevNum > rang:
                break
            metaRay.append(prevNum)
            k = k + 1
            prevNum = prevNum + metaVarOdd
            metaVarOdd = metaVarOdd + 2
            if prevNum > rang:
                break
            metaRay.append(prevNum)
            prevNum = prevNum + metaVarFact
            metaVarFact = metaVarFact + m
    return metaRay

def metaKlaubber(n):
    global mkAR
    mkAR=[]
    r=n+100000
    while len(mkAR)<n:
        klauNums = klaubberNumArray(r)
        metaNums = {}
        k = 1
        while True:
            mm = meta(k,r)
            if len(mm) == 0:
                break
            for m in mm:
                metaNums[m] = k
            k = k+1
        secondaryFilters = fMeta(r)
        for m in secondaryFilters:
            metaNums[m] = -1
        for i in range(len(klauNums)):
            num = klauNums[i]
            #print(num)
            isMeta = metaNums[i] if i in metaNums else None
            isPrimeNum = isPrime(num)
            #print(isPrimeNum)
            if isMeta == None and not isPrimeNum:
                mkAR.append(i)
            #print "%d: %s %s %s" % (i,isMeta,isPrimeNum,num)
    return mkAR

if generation>1:
    filePath=os.path.dirname(__file__)
    filePath=filePath.split("/")
    if generation<10:
        filePath=str(os.path.join(filePath[0:-16]))
        filePath=filePath.strip("[").strip("]")
    else:
        filePath=str(os.path.join(filePath[0:-17]))
        filePath=filePath.strip("[").strip("]")
    rangePath=os.path.join(filePath, "Quadratic Storage", "range")
    with open(rangePath) as storeEx:
        klauRange=int(storeEx.read())

    quadRange=int((klauRange*generation)/(generation-1))
else:
    filePath=os.path.dirname(__file__)

    klauRange=generation*int(raw_input("Size Coefficient: "))
    newRangePath=os.path.join(filePath, "Quadratic Storage", "Range")
    rangeStorage=open(newRangePath, "w")
    rangeStorage.write(str(klauRange))
    rangeStorage.close()

quadsArray=[]
quadsOut=[]
quadsVars=[]
compKlau=metaKlaubber(klauRange)


def progressFunction(cK, r, g):
    if cK:
        return (((-100.0)/(r*g))*cK)+100
    return 0

klauber=Quadratic(1,-1,41)

polyStorageList=[Quadratic(0,0,0)]*5
bestScoreList=[0]*5

def bestList(quadratic, score):
    lowestScore = 100000
    lowestIndex = 100000
    for i in xrange(len(bestScoreList)):
        if lowestScore > bestScoreList[i]:
            lowestScore = bestScoreList[i]
            lowestIndex = i
    if score > lowestScore:
        bestScoreList[lowestIndex] = score
        polyStorageList[lowestIndex] = quadratic
        return (polyStorageList)
    return (polyStorageList)

def testPoly(q,array):
    maxArray = array[-1]
    score = 0
    for x in range(1,len(array)):
        value = q(x)
        if value>maxArray:
           break
        elif value in array:
           score += 1
        else:
           return -1
    return score

def bestPoly(array, cRange, lRange=None, sRange=None):
    if lRange is None: lRange = cRange
    if sRange is None: sRange = lRange
    bestScore = -1
    bestQuadratic = None
    for s in xrange(-sRange,sRange):
        for l in xrange(-lRange,lRange):
            if s==0 and l==0:
                continue
            for c in xrange(-cRange, cRange):
                q = Quadratic(s,l,c)
                score = testPoly(q, array)
                bestList(q, score)
                if score>bestScore:
                    bestScore = score
                    bestQuadratic = q
                    print("best Score %d for %s" % (bestScore, bestQuadratic))
    return bestQuadratic

def readFunction():
        global quadsVars
        ID0=fileName.split(".")
        ID0=ID0[1:-1]

        quadReference="Quads."+".".join(ID0)+".txt"
        storePath=os.path.join(filePath, "Quadratic Storage", quadReference)
        with open(storePath) as storeEx:
            quadsVars=storeEx.read()
        os.remove(storePath)
        quadsVars=quadsVars.strip("[").strip("]").replace(" ",'')
        quadsVars=quadsVars.split(",")

        for x in quadsVars:
            quadsVars[quadsVars.index(x)]=int(x)
        for x in xrange(int(len(quadsVars)/3)):
            quadsArray.append(Quadratic(quadsVars[x], quadsVars[x+1], quadsVars[x+2]))

        for function in quadsArray:
            for i in xrange(quadRange):
                quadsOut.append(function(i))
        for x in quadsOut:
            quadsOut[quadsOut.index(x)]=abs(x)
        for x in quadsOut:
            try:
                compKlau.remove(x)
            except:
                pass
        updateProgress(ID0)

def updateProgress(ID):
    progressPath=os.path.join(filePath, "Progress Storage", "progress."+".".join(ID)+".txt")
    newProgress=open(progressPath, "w")
    newProgress.write(str(progressFunction(len(compKlau), klauRange, generation)))
    newProgress.close()

bestPoly(compKlau, klauRange)

if generation>1:
    readFunction()

if len(compKlau)>0 and generation<3:

        newtext=open(__file__,"r").read()
        newgen=str(generation+1)
        folderName="Clone Wars/Gen "+newgen
        dirpath = os.path.join(filePath, folderName)
        newtext=newtext[:88]+newgen+newtext[newtext.find('\n',88):]

        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        for x in xrange(5):
            newQuadVars=[]
            targetPoly = polyStorageList[x]
            newQuadVars.append(targetPoly.square)
            newQuadVars.append(targetPoly.linear)
            newQuadVars.append(targetPoly.constant)
            identity=str(x+1)
            store=os.path.join(filePath,"Quadratic Storage/Quads."+newgen+fileName[fileName.find('.',13):-2]+identity+".txt")
            quadStorage = open(store, "w")
            quadStorage.write(str(quadsVars+newQuadVars))
            quadStorage.close()

            name=os.path.join(dirpath,fileName[:12]+newgen+fileName[fileName.find('.',13):-2]+identity+".py")
            newFunction=open(name,"w")
            newFunction.write(newtext)
            newFunction.close()

            time.sleep(5)

            subprocess.Popen(["python", name])

else:
    print "DONE"
