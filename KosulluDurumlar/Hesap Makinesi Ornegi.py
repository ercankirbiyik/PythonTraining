import math

print("""

Lütfen yapmak istediğiniz işlemi seçiniz:

1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
5 - Karesini bulma
6 - BMI değerini hesaplama
7 - Üçgenin alanını hesaplama
8 - Karenin alanını hesaplama
9 - Karekök bulma

Çıkmak için 0'a basınız

""")

Operation = int(input("Lütfen yapmak istediğiniz işlemi seçiniz : "))

if Operation == 1:
    sayi_1 = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_2 = int(input("Lütfen ikinci sayıyı giriniz : "))

    print ("Sonuç : ", sayi_1 + sayi_2)
elif Operation == 2:
    sayi_1 = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_2 = int(input("Lütfen ikinci sayıyı giriniz : "))

    print ("Sonuç : ", sayi_1 - sayi_2)
elif Operation == 3:
    sayi_1 = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_2 = int(input("Lütfen ikinci sayıyı giriniz : "))

    print ("Sonuç : ", sayi_1 * sayi_2)
elif Operation == 4:
    sayi_1 = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_2 = int(input("Lütfen ikinci sayıyı giriniz : "))

    print ("Sonuç : ", sayi_1 / sayi_2)
elif Operation == 5:
    sayi_1 = int(input("Lütfen bir sayı giriniz : "))

    print ("Sonuç : ", sayi_1 ** 2)
elif Operation == 6:
    kilo = float(input("Lütfen birinci sayıyı giriniz : "))
    boy = float(input("Lütfen ikinci sayıyı giriniz : "))

    print ("BMI değeriniz : ", kilo / (boy**2))
elif Operation == 7:
    taban = int(input("Lütfen taban uzunluğunu yazınız : "))
    yükseklik = int(input("Lütfen yükseklik uzunluğunu yazınız : "))

    print ("Üçgenin alanı : ", (taban * yükseklik)/2)
elif Operation == 8:
    kenar = int(input("Lütfen kenar uzunluğunu yazınız : "))

    print ("Karenin alanı : ", kenar * kenar)
elif Operation == 9:
    sayi = int(input("Lütfen bir sayı giriniz : "))

    print ("Girdiğiniz sayının karekökü : ", sayi ** 0.5)
elif Operation == 0:
    print ("Uygulamadan çıkılıyor...")
    exit()
else:
    print("Geçersiz işlem!!!")