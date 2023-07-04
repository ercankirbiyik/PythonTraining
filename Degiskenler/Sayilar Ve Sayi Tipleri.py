
# SAYILAR
# Integer(Tam Sayılar)
# Float(Ondalıklı Sayılar)
# Complex(Komplex Sayılar - A + Bj)

A = 10
print(type(A))

B = 99.9
print(type(B))

C = 45.j
print(type(C))


# MATH Operatörleri
    # Toplama +
    # Çıkarma -
    # Çarpma *
    # Bölme /
    # Kalan Bulma %
    # Üs **
    # Bölen Bulma //
    # Önce parantez içi, çarpma ve bölme toplama ve çıkarmadan önce yapılır, işlemler sağdan sola yapılır

num1 = 15
num2 = 13
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(4 ** 3)
print(num1 // num2)
# Karekök bulma
print(16**0.5)
print(8*2+4/3-5)

    # HİPOTENÜS HESAPLAYICI (A^2 + B^2 = C^2)
A = int(input("Lütfen birinci kenar uzunluğu giriniz: "))
B = int(input("Lütfen ikinci kenar uzunluğu giriniz: "))
C = ((A**2 + B**2)**0.5)
print("Hipotenüs uzunluğu : ", C)


    # BMI(BEDEN KİTLE ENDEKSİ) HESAPLAYICI
Boy = float(input("Lütfen boyunuzu giriniz: "))
Kilo = float(input("Lütfen kilonuzu giriniz: "))
BMI = Boy / Kilo **2
print("BMI(Beden Kitle Endeksi) : ", BMI)