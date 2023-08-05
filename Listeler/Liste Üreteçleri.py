"""
    Liste Üreteçleri : List Comprehension
        * Uzun ve yorucu süreçlerin ve hataların azaltılmasını sağlamak amacıyla daha kısa kod blokları yazmamızı sağlar.
"""

# Elemanları 1'den başlayıp 1000'e kadar olan bir liste oluşturalım
# Fakat her elemanı tek tek yazmak çok uzun ve yoruvu olacaktır.

# Döngü yardımı ile aşağıdaki gibi yapabiliriz

print("****************")
List = []

for i in range(1000): # Bu döngü bize 0'dan başlayıp 1000'e kadar olan elemanları barındıran listeyi oluşturacaktır.
    List += [i]
print("Döngü ile oluşturulan liste :", List)


# Döngü olmadan aşağıdaki gibi üreteç yardımı ile listemizi tek satır kod ile oluşturabiliriz.

print("****************")

List2 = [i for i in range(1000)]
print("Liste üreteci ile oluşturulan liste :", List2)

print("****************")

String = "Python"
List3 = [i*3 for i in String]   #Her bir Stringin üç(i*3) defa yazılıp liste haline getirilmesini söylüyoruz.
print(List3)                    #['PPP', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']