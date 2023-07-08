"""
    BREAK İFADESİ
        * break ifadesi ile devam eden fonksiyonu yarıda kesebiliriz.
        * Herhangi bir koşula bağlı kalmaksızın işlemin sonlandırılmasını sağlar.
"""

print("*** BREAK ÖRNEK 1 ***")
sayi = 0

while sayi < 15:
    print(sayi)
    sayi += 1

print("*** BREAK ÖRNEK 2 ***")
"""
ALTTAKİ ÖRNEKTE İF DÖNGÜSÜNDE SAYI 7 OLDUĞUNDA İŞLEM YAPMAYI BIRAKMASINI SÖYLEDİK
VE BÖYLECE İŞLEM 7'DE BİTTİ.
"""
sayi1 = 1
while sayi1 < 10:
    print(sayi1)
    if (sayi1 == 7):
        break
    sayi1 += 1

"""
Break ifadesi yanlızca içinde bulunduğu döngüyü sonlandırır.
İç içe döngüler varsa ve en içteki döngüde break kullanılmışsa yanlızcan en içteki döngü sona erer.
Diğer dış döngüler işlemlerini yapmaya devam eder.
"""
print("*** BREAK ÖRNEK 3 ***")
Liste = [1, 2, 3, 4, 5, 6, 7, 8]

for i in Liste:
    if i == 6:
        break
    print(i)



"""
    CONTINUE İFADESİ
        * Continue ifadesi kendisinden sonra gelen kodları es geçer ve doğrudan döngünün başına döndürmemizi sağlar
        * Yani koşul sağlandıktan sonra gerçekleştirelecek işlem gerçekleştirilmez ve döngünün başına döner.
        * For ve While döngüleri ile kullanılabilir.
"""


print("*** CONTINUE ÖRNEK 1 ***")

"""
Aşağıdaki örnekte for döngüsündeki if koşulunda i 4 ve 7 değerlerini alırsa yazdırmamasını istedik 
ve sonucumuz : 
1 2 3 5 6 8 9 10 şeklinde 4 ve 7 sayılarını içermeyecek şekilde dönmektedir.
"""
Liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in Liste1:
    if i == 4 or i == 7:
        continue
    print(i)


print("*** CONTINUE ÖRNEK 2 ***")

sayi2 = 0

while sayi2 < 20:
    if sayi2 == 2:
        sayi2 += 1
        continue
    print(sayi2)
    sayi2 += 1



"""
    PASS İFADESİ
        * Pass ifadesi koşul veya döngü yaratmak istediğimiz fakat içindekilere tam kara veremediğimiz durumlarda kullanılır.
        * Boş bir ifadedir, Komut çalışmaz.
        * Daha çok yer tutucu bir ifadedir.
"""

print("*** PASS ÖRNEK 1 ***")

"""
for sayı in range(35): şeklindeki bir for döngüsü hata alacaktır fakat içine pass yazdığımızda hata almayıp devam edecektir.
"""

for sayı in range(35):
    pass