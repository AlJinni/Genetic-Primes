from __future__ import division
import math

polyStorageList=[]
array=[]

class Quadratic:
    def __init__(self, square, linear, constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d,%d,%d)" % (self.square,self.linear,self.constant)

#Cite: Ben Shahar
class polyStorage(object):

    def __init__(self,score,deg0,deg1,deg2):
        assert type(score) == int
        self.score = score
        self.deg0Coefficient = deg0
        self.deg1Coeffficient = deg1
        self.deg2Coefficient = deg2
        if len(polyStorageList) < 10:
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

arrayType=raw_input("Array Type: ")
if arrayType!="custom":
    arrayMax=int(raw_input("Array Size: "))
    if arrayType=="evolution":
        ran=raw_input("Klaubber Range: ")
        klauEvolve(ran, exQuads)
    elif arrayType=="all":
        for x in xrange(arrayMax):
            array.append(x+1)
    elif arrayType=="prime":
        n=arrayMax+100000
        i=2
        while len(array)<arrayMax:
            if isPrime(i):
                array.append(i)
            i+=1
    elif arrayType=="composite":
        n=arrayMax+100000
        i=2
        while len(array)<arrayMax:
            if not isPrime(i):
                array.append(i)
            i+=1
else:
    array=raw_input("Array: ")
    array=array.split(", ")
    array=map(int, array)
crange=int(raw_input("Constant Range: "))
bestPoly(array, crange)
