"""
    Fonksiyon tanımlamamızı sağlayan uygulamadır.
    def ifadesini kullanmadan fonksiyon oluşturmamızı sağlar.
    Def kullanmayacağımız tek satırlık kodlarda kullanmalıyız
    Lambda fonksiyonu bir çok parametre alabilir fakat sadece bir değer döndürür.
    İç içe fonksiyonlarda Lambda fonksiyonu çok yararlıdır.
"""

# Def fonksiyonu ile normal bir şekilde fonksiyon oluşturuyoruz.
def sum(a, b):
    return a + b

print(sum(4, 7))


# Lambda fonksiyonu ile yukarıdaki işlemlerin aynısı yapan bir fonksiyon oluşturuyoruz.
sum2 = lambda a, b: a + b

print(sum2(12, 6))


"""
******** Lambda Örnekleri ********
"""


# Kendisine verdiğimiz string bir değeri sondan başa doğru yazacak bir fonksiyon oluşturalım
def Reverse(a):
    return a [::-1]

print(Reverse("ERCAN"))


Reverse2 = lambda a:a[::-1]

print(Reverse2("KIRBIYIK"))


