import random

def isPrime(x):
    if (x > 1):
        for i in range(2, x):
            if (x % i) == 0:
                return False            
    return True

def gcd(x,y):
    if x > y:
        var = y
    else:
        var = x
    for i in range(1, var+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i     
    return gcd

def generateKey(p, q):
    if (isPrime(p)) and (isPrime(q)):
        n = p * q
        totient = (p-1)*(q-1)
        pubKey = random.randrange(1, totient)
        c = gcd(pubKey,totient)
        while c != 1:
            pubKey = random.randrange(1,totient)
        c = gcd(pubKey,totient)

        for i in range (1,totient):
            if (pubKey*i) % totient == 1 :
                priKey = i
            else :
                priKey = -1
        # return public and private key
        return ((pubKey, n) , (priKey, n))
    else :
        return("p dan q bukan bilangan prima")

    
        
        
    