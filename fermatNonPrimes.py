from random import randint
from fractions import gcd

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
        x = pow(a, d, n)
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
