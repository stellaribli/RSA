        hasil = (int(P)**d)%n
        if hasil < 10:
            Plain = Plain + '000' + str(hasil) 
        elif hasil < 100:
            Plain = Plain + '00' + str(hasil) 
        elif hasil < 1000:
            Plain = Plain + '0' + str(hasil) 
        else:
            Plain = Plain + str(hasil) + ' '