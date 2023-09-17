'''
    #  Listelere benzerler
    #  İçeriği değiştirilemezler
    #  Verileri demetlerde saklayabilirler
'''

##########  Örnekler  ##########

Tuples_1 = "a", "b", "c", "d", "e", "f", "g"
print("Tuple_1 type = ", type(Tuples_1))
print("Tuple_1 = ", Tuples_1)

Tuples_2 = ('apple', 'orange', 'banana', 'pear', 'melon')
print("Tuple_2 type = ",type(Tuples_2))
print("Tuple_2 = ", Tuples_2)

Tuples_3 = (1, 3, 4, 7, 8, 11, 15, 17)
print("Tuple_3 type = ", type(Tuples_3))
print("Tuple_3 = ", Tuples_3)

Tuples_4 = (4,)
print("Tuple_4 type = ", type(Tuples_4))
print("Tuple_4 = ", Tuples_4)

Tuples_5 = (4)
print("Tuple_5 type = ", type(Tuples_5))
print("Tuple_5 = ", Tuples_5)

Tuples_6 = ('London')
print("Tuple_6 type = ", type(Tuples_6))
print("Tuple_6 = ", Tuples_6)
print(tuple(Tuples_6))

Tuples_7 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print("Tuple_7 type = ", type(Tuples_7))
print("Tuple_7 = ", Tuples_7)
print(Tuples_7[3])                                 # Demetteki belirli bir elementi getirmemizi sağlayan fonksiyondur

'''
    # DEMETLER SADECE OKUNABİLİR OBJELER OLDUKLARI İÇİN LİSTELERDEN HIZLI ÇALIŞIRLAR
    # PARANTEZ İÇİNDE BELİRTİLMELERİ OPSİYONELDİR
    # ELEMENTLERİ AYIRMAK İÇİN VİRGÜL KULLANILMASI ZORUNLUDUR
    # GENELDE PROBRAMLARIN CONFİG DOSYALARINDA TANIMLANIR
'''

'''
    DEMET İŞLEMLERİ
        # İÇERİĞİ DEĞİŞTİRİLEMEDİĞİ İÇİN YAPILABİLECEK İŞLEM SAYISI AZDIR
        # TOPLAMA(+) VE ÇARPMA(*) İŞLEMLERİ YAPILABİLİR
        
'''

Tuples_8 = Tuples_1 + Tuples_2
print("Tuple_8 = ", Tuples_8)

Tuples_9 = Tuples_3 * 3
print("Tuples_9 = ", Tuples_9)

'''
    TUPLES ELEMAN EKLEME İŞLEMLERİ YAPAMAZ
    
    Aşağıdaki örnekte : 
          Tuples_4 [0] = 'watermelon'
            print(Tuples_4)
        
        # 'TypeError: 'tuple' object does not support item assignment' hatası verir!!!
        
        Bu sorunu aşağıdaki örnekte olduğu gibi yeni bir tuple oluşturup eklemek istediğimiz elemanı ve 
            eski tuple ile toplarız.
'''

# Tuples eleman ekleme işlemi örneği

Tuples_10 = "watermelon",
print("Tuples_10 = ", Tuples_10)

Tuples_11 = Tuples_4 + Tuples_10
print("Tuples_11 = ", Tuples_11)


'''
    DEMET METODLARI
        # INDEX()
        # COUNT()
        # LEN()...
'''

# İNDEX()
print("b elemanının indexi = ", Tuples_1.index("b"))

# COUNT()
print("Tekrar eden 'o' harflerinin sayısı = ", Tuples_6.count("o"))

# LEN()
print("Demetin uzunluğu, eleman sayısı = ", len(Tuples_1))