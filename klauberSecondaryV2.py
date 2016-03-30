import math

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
    for s in range(sRange):
        for l in range(lRange):
            if s==0 and l==0:
                continue
            for c in range(cRange):
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
    for x in range(1,len(array)):
        value = q(x)
        if value>maxArray:
           break
        elif value in array:
           score += 1
        else:
           return -1
    return score

def bestPolySet(array,cRange,lRange,sRange):
    polySet = []
    while len(array)>0:
        q = bestPoly(array, cRange, lRange, sRange)
        polySet.append(q)
        for x in range(1,len(array)):
            v = q(x)
            if v in array:
               array.remove(v)
        print("New Array length %d" % len(array))
    return polySet

def subPoly(array, poly):
    currentVal = None
    for i in range(0, len(array)):
        currentVal = poly(i)
        if not currentVal > array[len(array)-1]:
            if currentVal in array:
                array.remove(currentVal)
    return array

def kNPsubIP(number, IP):
    array = klauberNotPrime(number)
    for i in range(len(IP)):
        array = subPoly(array, IP[i])
    return array

def repRun(number, it):
    tedCruz = [Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0)]
    for i in range(it):
        tedCruz[i] = bestPoly(kNPsubIP(number, tedCruz), 2000, 200, 20)
    print(tedCruz)

def repRunEx(number, it):
    tedCruz = [Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0), Quadratic(0,0,0)]
    for i in range(it):
        print(kNPsubIP(number+(i*41), tedCruz))
        tedCruz[i] = bestPoly(kNPsubIP(number+(i*41), tedCruz), 2000, 200, 20)
    print(tedCruz)

donaldTrump = [Quadratic(1,0,41)]
print(kNPsubIP(200, donaldTrump))
#bestPoly(kNPsubIP(200, donaldTrump), 2000, 200, 20)
repRunEx(82, 4)
