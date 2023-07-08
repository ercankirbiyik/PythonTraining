"""
Liste ve in operatörleri

Liste yapısı : String ve sayılar kümesidir.

in operatörleri : Bir elemanın belirtilen bir veri kümesinde olup olmadığını kontrol eder.

"""

print("h" in "hello")  #Sonucumuz True olarak dönecektir.
print("lo" in "hello")  #Sonucumuz True olarak dönecektir.
print("be" in "hello")  #Sonucumuz False olarak dönecektir.


"""
For : listelerdeki değerler üzerinde gezinmemizi ve yinelememizi sağlayan bir döngü tipidir.
"""

# Liste elemanlarının for döngüsü ile yazdırılması
liste = [1, 2, 3, 4, 5, 6, 7]

for i in liste:
    print(i)


# Listeki elemanların for döngüsü ile toplamlarının alınması
Toplam = 0

for i in liste:
    Toplam += i
    """ 
    Eğer print işlemini bu satırda üstteki Toplam satırı ile aynı hizada yazarsam 
    print("Liste elemanlarının toplamı : ", Toplam) şeklinde
    for döngüsünün içinde her döndüğünde bana dönen elemenların toplamını verecekti.
    """

print("Liste elemanlarının toplamı : ", Toplam)



# Liste içindeki çift sayıları veren örnek
liste2 = [2, 4, 39, 11, 90, 123, 234, 1993, 1881, 2382398]

for i in liste2:
    if i % 2 == 0:   # Buradaki if ile 2'ye bölündüğünde 0 kalanını veren sayıların alınacağını belirttik.
        print(i)



# String karakterlerde for döngüsü
S = "Python"

for i in S:  # Bu for döngüsü bütün karakterleri tek tek yazdırır
    print(i)


for i in S:  # Bu for döngüsü bütün karakterleri üçer kez yazdırır
    print(i * 3)