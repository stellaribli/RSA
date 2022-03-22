c = 0 #cipherteks
m = '' #plainteks
d = 1019 #kunci dekripsi
e = 79 #kunci enkripsi
n = 3337 #p*q
concatM = 0

def convertPlainText(m):
    m = m.replace(" ","")
    M = ''
    for i in range (len(m)):
        if ord(m[i])>90:
            concatM = ord(m[i])-97
        else:
            concatM =ord(m[i])-65
        if concatM > 9:
            M = M + str(concatM)
        else:
            M = M + '0' + str(concatM)
    return M

def encrypt (M,e,n):
    Cipher = ''
    C = ''
    hasil = ''
    for i in range(len(M)//4):
        C = M[i*4:((i*4)+4)]
        hasil = (int(C)**e)%n
        if hasil < 10:
            Cipher = Cipher + '000' + str(hasil) + ' '
        elif hasil < 100:
            Cipher = Cipher + '00' + str(hasil) + ' '
        elif hasil < 1000:
            Cipher = Cipher + '0' + str(hasil) + ' '
        else:
            Cipher = Cipher + str(hasil) + ' '
    if (len(M)//4 != len(M)/4):
        C = M[(i*4)+4:(i*4)+6]
        hasil = (int(C)**e)%n
        if hasil < 10:
            Cipher = Cipher + '000' + str(hasil) + ' '
        elif hasil < 100:
            Cipher = Cipher + '00' + str(hasil) + ' '
        elif hasil < 1000:
            Cipher = Cipher + '0' + str(hasil) + ' '
        else:
            Cipher = Cipher + str(hasil) + ' '
    return Cipher

def decrypt (C,d,n):
    C = C.replace(' ','')
    Plain = ''
    P = ''
    hasil = ''
    for i in range(len(C)//4):
        P = C[i*4:((i*4)+4)]
        hasil = (int(P)**d)%n
        if hasil < 10:
            Plain = Plain + '000' + str(hasil) 
        elif hasil < 100:
            Plain = Plain + '00' + str(hasil) 
        elif hasil < 1000:
            Plain = Plain + '0' + str(hasil) 
        else:
            Plain = Plain + str(hasil)
    return Plain

M = convertPlainText('HELLO ALICE')
enkr = (encrypt(M,e,n))
print(enkr)
print(decrypt(enkr,d,n))
# print ((4//2)==(4/2))
# print(5//2)