import math
import itertools
import time
import sys

def klauber(x):
    return x*x-x+41

# Prime Checker from http://pages.physics.cornell.edu/~sethna/StatMech/ComputerExercises/PythonSoftware/Primes.py
def isPrime(n):
    Dmax = math.sqrt(n)
    if n == 2:
        return True
    if n%2 == 0:
        return False
    d = 3
    while n%d != 0 and d <= Dmax:
        d += 2
    return d > Dmax

def klauberNotPrime(r):
    result = []
    for i in xrange(1,r):
        if not isPrime(klauber(i)):
            result.append(i)
    return result

class Quadratic:
    def __init__(self, square,linear,constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d,%d,%d)" % (self.square,self.linear,self.constant)

# Find best ploynomial which matches all terms in array

def bestPoly(array, cRange, lRange=None, sRange=None):
    if lRange is None: lRange = cRange
    if sRange is None: sRange = lRange
    bestScore = -1
    bestQuadratic = None
    for s in xrange(sRange):
        for l in xrange(lRange):
            if s==0 and l==0:
                continue
            for c in xrange(cRange):
                q = Quadratic(s,l,c)
                score = testPoly(q, array)
                if score>bestScore:
                    bestScore = score
                    bestQuadratic = q
                    print("best Score %d for %s" % (bestScore, bestQuadratic))
    return bestQuadratic

def testPoly(q,array):
    maxArray = array[-1]
    score = 0
    for x in xrange(1,len(array)):
        value = q(x)
        if value>maxArray:
           break
        elif value in array:
           score += 1
        else:
           return -1
    return score

#Calculates a string of the best polynomials in sequence - similar to repRunEx but without replacement/supplementation of the array passed
def bestPolySet(array,cRange,lRange,sRange):
    polySet = []
    while len(array)>0:
        q = bestPoly(array, cRange, lRange, sRange)
        polySet.append(q)
        for x in xrange(1,len(array)):
            v = q(x)
            if v in array:
               array.remove(v)
        print("New Array length %d" % len(array))
    return polySet

#Subtracts a given polynomial from a given array, and returns the result
def subPoly(array, poly):
    currentVal = None
    for i in xrange(0, len(array)):
        currentVal = poly(i)
        if not currentVal > array[len(array)-1]:
            if currentVal in array:
                array.remove(currentVal)
    return array

def kNPsubIP(number, IP):
    array = klauberNotPrime(number)
    for ip in IP:
        array = subPoly(array, ip)
    return array

def repRunEx(number, it):
    tedCruz = [Quadratic(0,0,0)] * it
    for i in xrange(it):
        print(kNPsubIP(number+(i*41), tedCruz))
        tedCruz[i] = bestPoly(kNPsubIP(number+(i*41), tedCruz), 2000, 200, 20)
    print(tedCruz)


#The following two arrays are for use by the BestList
bestQuadList = [Quadratic(0,0,0)] * 5

bestScoreList = [0] * 5

#Quadratics for testing functions
a = Quadratic(1,1,1)
b = Quadratic(2,2,2)
c = Quadratic(3,3,3)
d = Quadratic(4,4,4)
e = Quadratic(5,5,5)

def bestList(quadratic, score):
    lowestScore = sys.maxint
    lowestIndex = sys.maxint
    for i in xrange(len(bestScoreList)):
        if lowestScore > bestScoreList[i]:
            lowestScore = bestScoreList[i]
            lowestIndex = i
    if score > lowestScore:
        bestScoreList[lowestIndex] = score
        bestQuadList[lowestIndex] = quadratic
        return (bestQuadList)
    return (bestQuadList)

def bestPolyLoop(kArray, cRange, lRange=None, sRange=None):
    global bestQuadList
    global bestScoreList
    bestQuadList = [Quadratic(0,0,0)] * 5
    bestScoreList = [0] * 5
    bestListReceived = []
    if lRange == None: lRange = cRange
    if sRange == None: sRange = lRange
    for s in xrange(sRange):
        for l in xrange(lRange):
            if s==0 and l==0:
                continue
            for c in xrange(cRange):
                q = Quadratic(s,l,c)
                score = testPoly(q, kArray)
                bestListReceived = bestList(q, score)
    return bestListReceived


#def pseudoGenetics(layers, krange, kInc, cRange, lRange, sRange, currentlyExcludedQuads):
 #   tL = []
  #  for i in xRange(layers):
   #     tL += bestPolyLoop(krange, cRange, lRange, sRange)


def layerScore(path, krange, cRange, lRange, sRange):
    arrayToTrim = metaKlaubber(krange)
    importantPolyList = []
    for i in xrange(len(path)):
        regularPolyList = bestPolyLoop(arrayToTrim, cRange, lRange, sRange)
        #print(regularPolyList)
        importantPoly = regularPolyList[path[i]]
        #print(path[i])
        #print(importantPoly)
        #print("The array length before subtraction is: " + str(len(arrayToTrim)))
        arrayToTrim = subPoly(arrayToTrim, importantPoly)
        #print("The array length after subtraction is: " + str(len(arrayToTrim)))
        #print(arrayToTrim)
        importantPolyList.append(importantPoly)
    return len(arrayToTrim)

def fixedPseudoGenetics(krange, cRange, lRange, sRange, recWidth):
    lowestScore = sys.maxint
    bestTriple = [9999] * 5
    currentTime = 0
    for path in set(itertools.permutations([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],5)):
        print("The current Path is: " + str(path))
        print time.clock() - currentTime
        currentTime = time.clock()
        tScore = layerScore(path, krange, cRange, lRange, sRange)
        if lowestScore > tScore:
            print(lowestScore)
            print(tScore)
            lowestScore = tScore
            for i in xrange(len(path)):
                bestTriple[i] = path[i]
    return bestTriple



#Make an array of the klauberNotPrimes up to the krange
#Find the top polynomials with bestPolyLoop
#Call self with first element of array as currentlyExcludedQuads, and with layers = layers - 1
#If layers = 0 print the string of

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################

#META EXTRACTOR FUNCTIONS BELOW, RETURNS REMAINING VALUES AFTER SUBTRACTION OF THE FIRST TWO INFINITE FAMILIES, CALL WITH metaKlaubber(r)#

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################

#metaKlaubber still needs to be converted


#Call complete program with metaKlaubber(limit)





import math

#An array of values for the q function to return
qFunction = (6, 10, 12, 14, 15, 18, 20, 21, 22, 24, 26, 28, 30, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 111, 112)

#Indexes at ZERO: Limit 0<=n<=100: A function that will return the value of q for a given n (see "prime stuffs" google document)
def q(n):
    return qFunction[(n-1)]

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
        floorN = math.floor(n/2)+1
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
# Prime Checker from http://pages.physics.cornell.edu/~sethna/StatMech/ComputerExercises/PythonSoftware/Primes.py
def isPrime(n):
    Dmax = math.sqrt(n)
    if n == 1 or n == 2:
        return True
    if n%2 == 0:
        return False
    d = 3
    while n%d != 0 and d <= Dmax:
        d += 2
    return d > Dmax


class Quadratic:
    __slots__ = ['square', 'linear', 'constant']

    def __init__(self, square,linear,constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant

    def __repr__(self):
        return "Quadratic(%d,%d,%d)" % (self.square,self.linear,self.constant)

def klaubberNumArray(r):
    result = [0] * r
    k = Quadratic(1, -1, 41)
    for i in xrange(r):
        result[i] = (k(i))
    return result

def meta(n, lim):
    k = Quadratic(1, -1, 41)
    metaRay = []
    if n==1:
        i = 0
        while True:
            metaVar = i * i + 41
            if (metaVar > lim):
                break
            metaRay[:0] = [metaVar]
            i = i + 1
        return metaRay
    if n==2:
        j = 1
        while True:
            metaVar = ((j * (j - 1)) / 2) + 82
            if metaVar > lim:
                break
            metaRay[:0] = [metaVar]
            j = j + 1
        return metaRay
    m = 2 * (n-1)
    metaVarOdd = 1
    metaVarFact = m
    prevNum = 41 * n
    k = 0
    while True:
        if prevNum > lim:
            break
        metaRay[:0] = [prevNum]
        k = k + 1
        prevNum = prevNum + metaVarOdd
        metaVarOdd = metaVarOdd + 2
        if prevNum > lim:
            break
        metaRay[:0] = [prevNum]
        prevNum = prevNum + metaVarFact
        metaVarFact = metaVarFact + m
    return metaRay


def metaKlaubber(r):
    allTheIs = []
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
    for i in xrange(len(klauNums)):
        num = klauNums[i]
        #print(num)
        isMeta = metaNums[i] if i in metaNums else None
        isPrimeNum = isPrime(num)
        #print(isPrimeNum)
        if isMeta == None and not isPrimeNum:
            allTheIs.append(i)
        #print "%d: %s %s %s" % (i,isMeta,isPrimeNum,num)
    return allTheIs




donaldTrump = [Quadratic(1,0,41)]
print(kNPsubIP(200, donaldTrump))
#bestPoly(kNPsubIP(200, donaldTrump), 2000, 200, 20)
#repRunEx(82, 3)
bPath = fixedPseudoGenetics(1400, 1400, 400, 100, 4)
print (bPath)
print layerScore(bPath, 1400, 1400, 400, 100)

#1500, 1500, 500, 100
