"""
***KARŞILAŞTIRMA OPERATÖRLERİ***

    * Eşittir        ==
    * Eşit değildir  !=
    * Küçüktür       <
    * Büyüktür       >
    * Büyük eşittir  >=
    * Küçük eşittir  <=
Sonuçlar true-false olarak döner
"""

print("Ercan" == "Ercan") # Sonuç true olarak döner
print("Ercan" == "John") # Sonuç false olarak döner

print("Ercan" != "John") # Sonuç true olarak döner
print("Ercan" != "Ercan") # Sonuç false olarak döner

# Python stringlerde küçük-büyük karşılaştırması yaparken alfabetik sıraya göre yaptığı için en son harf en büyük şeklinde yapılır
print("Ercan" > "John") # Sonuç false olarak döner
print("Ercan" < "John") # Sonuç true olarak döner
print(5 < 7) # Sonuç true olarak döner
print(5 > 7) # Sonuç false olarak döner

print(5 <= 7) # Sonuç true olarak döner
print(5 >= 7) # Sonuç false olarak döner

# print(5 < "Ercan") bu tür bir karşılaştırma hata verir, Sebebi ise farklı tipteki verileri karşılaştıramamasıdır. String vs Integer


"""
***MANTIKSAL OPERATÖRLER***

    * And  = Eğer iki karşılaştırma da true ise true döner, değilse false döner
    * Or   = Karşılaştırmalardan herhangi biri true ise true döner, her ikisi de false ise false döner
    * Not  = Sonuç değiştirme operatörü. True olan bir sonucu not operatörü ile false yapabiliriz
"""
# AND
print(5 == 5 and "John" < "David") # False
print(5 <= 7 and "John" == "John") # True
print(15 == 1 and 1 < 5) # False

# OR
print(5 == 5 or "John" < "David") # True
print(5 == 5 or "John" > "David") # True
print(5 != 5 or "John" < "David") # False
print(5 != 5 or "John" > "David") # True

# NOR
print(not 5 == 5 ) # False
print(not "John" < "David") # True
print(not 10 < 100000) # False
print(not 10 > 100000) # True