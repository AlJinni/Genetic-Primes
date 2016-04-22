import sys,numpy
def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(numpy.sqrt(n))+1)
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1
    return primes

def condense(L):
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count = count + 1
    else:
      if prime != 0:
        list = list + [str(prime) + '^' + str(count)]
      prime,count=x,1
  list = list + [str(prime) + '^' + str(count)]
  return list

print factorize(int(sys.argv[1]))
