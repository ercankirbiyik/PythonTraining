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


print("Fibonacci Dizisi Örneği : ")

"""
    Fibonacci Dizisi
        * Dizideki her sayı kendinden önceki iki sayının toplamına eşittir.

"""

Number1 = 1
Number2 = 3

Fibonacci = []

for value in range(20):
    Number1, Number2 = Number2, Number1 + Number2   # Burada başta atadığımız değerlere göre Number1 ve Number2 sayılarının toplamını
                                                    # bir sonraki sayıya atayarak bir döngü oluşturup Fibonacci serisi oluşturduk.
    Fibonacci.append(Number2)
print("Döngü ile oluşturduğumuz Fibonacci Dizisi", Fibonacci) #[4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603]