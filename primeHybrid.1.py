from __future__ import division
import random, sys, os, tempfile, subprocess, math

generation=1

import time
fileName=os.path.basename(__file__)

polyStorageList=[]
compKlau=[]
if generation>1:
    filePath=os.path.dirname(__file__)
    filepath=filePath.split("/")
    if generation<10:
        filePath=os.path.join(filePath[0:-16])
    else:
        filePath=os.path.join(filePath[0:-17])
    rangePath=os.path.join(filePath, "Quadratic Storage", "Range")
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

class Quadratic:
    def __init__(self, square, linear, constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d,%d,%d)" % (self.square,self.linear,self.constant)

klauber=Quadratic(1,-1,41)

#Cite: Ben Shahar
class polyStorage(object):

    def __init__(self,score,s,l,c):
        assert type(score) == int
        self.score = score
        self.square = s
        self.linear = l
        self.constant = c
        if len(polyStorageList) < 5:
            polyStorageList.append(self)
        else:
            scoreList = []
            for function in polyStorageList:
                scoreList.append(function.score)
            minimum = min(scoreList)
            if minimum < self.score:
                for index, score in enumerate(scoreList):
                    if score == minimum:
                        polyStorageList.remove(polyStorageList[index])
                        break
                polyStorageList.append(self)

def isPrime(x):
    for i in range(2,1+int(math.sqrt(x))):
        if x%i == 0:
           return False
    return True

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
                qstore=polyStorage(score,s,l,c)
                if score>bestScore:
                    bestScore = score
                    bestQuadratic = q
                    print("best Score %d for %s" % (bestScore, bestQuadratic))
    return bestQuadratic
i=2
while len(compKlau)<(klauRange):
    if not isPrime(klauber(i)):
        compKlau.append(i)
    i=i+1

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

bestPoly(compKlau, klauRange)

if generation>1:
    readFunction()

if len(compKlau)>0:

        newtext=open(__file__,"r").read()
        newgen=str(generation+1)
        folderName="Clone Wars/Gen "+newgen
        dirpath = os.path.join(filePath, folderName)
        newtext=newtext[:95]+newgen+newtext[newtext.find('\n',95):]

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
