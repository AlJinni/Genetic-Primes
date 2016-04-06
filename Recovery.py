import math
import itertools

def klauber(x):
    return x*x-x+41

def isPrime(x):
    for i in range(2,1+int(math.sqrt(x))):
        if x%i == 0:
           return False
    return True

def klauberNotPrime(r):
    result = []
    for i in range(1,r):
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
    lowestScore = 100000
    lowestIndex = 100000
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
    arrayToTrim = klauberNotPrime(krange)
    importantPolyList = []
    for i in xrange(len(path)):
        regularPolyList = bestPolyLoop(arrayToTrim, cRange, lRange, sRange)
        #print(regularPolyList)
        #print(path)
        #print(i)
        importantPoly = regularPolyList[path[i]]
        #print(path[i])
        print(importantPoly)
        #print("The array length before subtraction is: " + str(len(arrayToTrim)))
        arrayToTrim = subPoly(arrayToTrim, importantPoly)
        #print("The array length after subtraction is: " + str(len(arrayToTrim)))
        #print(arrayToTrim)
        importantPolyList.append(importantPoly)
    return len(arrayToTrim)
    
def fixedPseudoGenetics(krange, cRange, lRange, sRange, recWidth):
    lowestScore = 1000000000
    bestTriple = [9999] * 5
    for a in xrange(recWidth):
        for b in xrange(recWidth):
            for c in xrange(recWidth):
                for d in xrange(recWidth):
                    for e in xrange(recWidth):
                        path = [a,b,c,d,e]
                        print(path)
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
                
