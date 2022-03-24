import random

# def convert(s): # Convert string to ASCII
#     return ([ord(c) for c in s])

def gcd(x,y):
    if x > y:
        var = y
    else:
        var = x
    for i in range(1, var+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i     
    return gcd

# def isPrime(x):
#     found=False
#     if (x > 1):
#         for i in range(2, x):
#             if (x % i) == 0:
#                 found= False 
#         found = True
#     # return found 
def isPrime(x):
    check =False
    if x == 1:
        check = False
    elif x == 2:
        check = True
    else:
        for i in range (2, x):
            if (x % i == 0):
                check = False
        check = True

    if check == False:
        print("bukan prima")
    else:
        print(" prima")

# def isInputPrime(x,y):
#     if (isPrime(x) and isPrime(y) == True):
    

def generateKey(p, q):
    if (isPrime(p) and (isPrime(q) == False)):
        raise Exception("p dan q harus prima")
        
    elif (isPrime(p)) and (isPrime(q)): # jika p dan q sudah prima
    
        n = p * q
        totient = (p-1)*(q-1)

        # generate public key
        pubKey = random.randrange(1, totient)
        e = gcd(pubKey,totient)
        while e != 1:
            pubKey = random.randrange(1,totient)
            e = gcd (pubKey,totient)
        
        # generate private key
        found = 0
        k = 1
        while not(found):
            priKey = (1+k*totient)/pubKey
            if ((pubKey*int(priKey))%totient == 1):
                found = 1    
            k = k+1
        priKey = int(priKey)
        print (str(pubKey)+" "+str(priKey)+" "+ str(n))
        # else:
        #     print("p dan/atau q bukan prima")

        # export public dan private key
        file_pubkey = open('PublicKey.pub', 'w')
        file_pubkey.write(str(pubKey))
        file_pubkey.write(" ")
        file_pubkey.write(str(n))
        file_pubkey.close()

        file_prikey = open('PrivateKey.pri', 'w')
        file_prikey.write(str(priKey))
        file_prikey.write(" ")
        file_prikey.write(str(n))
        file_prikey.close()

isPrime(24)
# generateKey(20,40)

