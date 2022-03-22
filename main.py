c = 0 #cipherteks
m = '' #plainteks
d = 0 #kunci dekripsi
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
    # length = int(len(M)/4)
    # print(length)
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

M = convertPlainText('HELLO ALICE')
print(encrypt(M,e,n))

# print ((4//2)==(4/2))
# print(5//2)