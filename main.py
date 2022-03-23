from time import process_time
import os
c = 0 #cipherteks
m = '' #plainteks
d = 1019 #kunci dekripsi
e = 79 #kunci enkripsi
n = 3337 #p*q
concatM = 0
t1 = 0
t2 = 0

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
    t1 = process_time()
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
    t2 = process_time()
    t = t2-t1
    Cipher = hex(int(Cipher.replace(' ','')))
    file = open('HasilKonversiEncrypt.txt', 'w')
    file.write(Cipher)
    file.close()
    file_size = os.stat('HasilKonversiEncrypt.txt')
    return Cipher, t, file_size

def decrypt (C,d,n):
    t1 = process_time()
    C = str(C).replace(' ','')
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
    t2 = process_time()
    t = t2-t1
    file = open('HasilKonversiDecrypt.txt', 'w')
    file.write(Plain)
    file.close()
    file_size = os.stat('HasilKonversiDecrypt.txt')
    
    return Plain, t, file_size

M = convertPlainText('HELLO ALICE')
enkr = (encrypt(M,e,n))
# print(hex(int(enkr.replace(' ',''))))

print((encrypt(M,e,n))[0]) # hasil enkripsi
print((encrypt(M,e,n))[1]) # waktu enkripsi dalam detik
# enkr = encrypt(M,e,n)[0]
# print(hex(int(enkr.replace(' ','')))) #hasil enkripsi dlm hexa
# print(decrypt(enkr,d,n)[0]) # hasil dekripsi
# print(decrypt(enkr,d,n)[1]) # waktu dekripsi dalam detik
# print ('Waktu Dekripsi ' + str(t2-t1) +' detik')
# print ((4//2)==(4/2))
# print(5//2)