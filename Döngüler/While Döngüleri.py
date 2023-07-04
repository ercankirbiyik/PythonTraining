
"""
i değişkenini sıfır değeriyle başlatıp
While döngüsü ile birer birer 14'e kadar arttırdık.

Döngüyü sonlandırmak için işlemin sonuna i += 1 gibi bir ifade bırakılması gerekmektedir.
Aksi taktirde sonsuz döngüye girecektir.
"""

print("**** ÖRNEK - 1 ****")
i = 0
while i < 15:
    print(i)
    i += 1

print("**** ÖRNEK - 2 ****")
i = 0
while i < 20:
    print(i)
    i += 2

print("**** ÖRNEK - 3 ****")
i = 0
while i < 20:
    print(i, " - HELLO WORLD")
    i += 1
