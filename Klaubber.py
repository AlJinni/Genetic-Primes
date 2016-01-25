import math

class Quadratic:
    def __init__(self, square, linear, constant):
        self.square = square
        self.linear = linear
        self.constant = constant

    def __call__(self, x):
        return self.square*x*x + self.linear*x + self.constant
    
    def __repr__(self):
        return "Quadratic(%d, %d, %d)" % (self.square, self.linear, self.constant)

def klaubber(x):
    return x*x - x + 41
    
def isPrime(x):
    for i in range(2, int(math.ceil(math.sqrt(x))) + 1):
        if x % i == 0:
            return False
    return True
        
def klauNotPrime(r):
    result = []
    for i in range(1, r):
        if not isPrime(klaubber(i)):
            result.append(i)
    return result

def bestPoly(slCoMax, cCoMax, array):
    percentDone = 0
    bestFit = 0
    bestQuad = None
    for a in range(-slCoMax, slCoMax):
        for b in range(-slCoMax, slCoMax):
            if a==0 and b==0:
                continue
            percentDone = .1 * (a+500) + .0001 * (b+500)
            print percentDone
            for c in range(-cCoMax, cCoMax):
                curQuad = Quadratic(a,b,c)
                fitness = inBounds(curQuad, array)
                if fitness > bestFit:
                    bestFit = fitness
                    print bestFit
                    bestQuad = Quadratic(a,b,c)
    print bestFit
    print bestQuad
    return bestQuad


def inBounds(curQuad, array):
    polyOut = []
    fitness = 0
    for i in range(0, len(array)):
        polyOut.append(curQuad(i))
        if not polyOut[i] > array[len(array)-1]:
            if polyOut[i] in array:
                fitness+=1
            else:
                return -1
    return fitness

def subPoly(array, poly):
    currentVal = None
    for i in range(0, len(array)):
        currentVal = poly(i)
        if not currentVal > array[len(array)-1]:
            if currentVal in array:
                array.remove(currentVal)
    return array

def main(array, numIt, slCoMax, cCoMax):
    bestPolies = []
    for i in range(0, numIt):
        polyToSub = bestPoly(slCoMax, cCoMax, array)
        bestPolies.append(polyToSub)
        array = subPoly(array, polyToSub)
    print len(array)
    return bestPolies
#def bestPoly(r, array):
    #
