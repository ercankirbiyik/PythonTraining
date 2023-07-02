    # Veri Tipi Dönüşümleri
        # float()
        # int()
        # str()

A = 23
print(A)
# float(A) fonksiyonu ile integer olan değeri floata çevirdik
A = float(A)
print(A)

B = 12.0
print(B)
# int(B) fonksiyonu ile float olan değeri integera çevirdik
B = int(B)
print(B)

C = 2342313
print(type(C))
print(C)
# Tipi int olan C değişkenini str(C) fonksiyonu ile string tipine çevirdik
C = str(C)
print(type(C))
print(C)

D = "123123123"
print(type(D))
print(D)
# Tipi string olan D değişkenini int(D) fonksiyonu ile integer tipine çevirdik
# Burada dikkat edilmesi gereken şey :
    # int veya float tipine çevrilecek değişkenin bütün karakterleri numerik olmalıdır!!!
D = int(D)
print(type(D))
print(D)

E = "9876"
print(type(E))
print(E)
#
E = float(E)
print(type(E))
print(E)

