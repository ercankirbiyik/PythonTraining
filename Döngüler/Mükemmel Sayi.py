"""
Mükemmel sayı, ardışık sayıların toplamından (1+2+3=6 Mükemmel sayıdır) elde edilen sayıdır.
    Döngülerimizde kullanıcıdan alınan sayının "değer" sayısı ile oranlayıp "toplam" sayısı
    üzerinden mükemmel sayı olup olmadığı kontrol edilier.
"""


sayi = int(input("Lütfen bir sayı giriniz: "))

deger = 1
toplam = 0

while deger < sayi:
    if sayi % deger ==0:
        toplam += deger
    deger += 1

if toplam == sayi:
    print(sayi, "mükemmel sayıdır...")

else:
    print(sayi, "mükemmel bir sayı değildir...")