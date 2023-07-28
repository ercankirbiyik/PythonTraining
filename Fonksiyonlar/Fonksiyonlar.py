"""
    Belli işlevleri tekrar tekrar kullanmamızı sağlayan birleşik işlemler
    Örneğin print() çıktı almamızı sağlayan bir fonksiyondur.
    Karmaşık işlemleri tek adımda yapmamızı sağlayan hazır şablonlardır ve sadece çağırılınca çalışırlar.
"""


"""
    Fonksiyon Tanımlama ve Çağırma
        Tanımlama : 
            def Fonksiyon_Adi(parametre):
            işlemler
            "
            "
            return
"""


# Rehbere kişi ekleme örneği

def Add_Contact(Name, Surname, PhoneNumber, emailAddress):
    print("Name = ", Name, "\nSurname = ", Surname, "\nPhone Number = ", PhoneNumber, "\nEmail Address = ", emailAddress)



Add_Contact("Ercan", "Kırbıyık", "099999", "ercan@kirbiyik.com")
# Fonksiyonumuzdaki parametrelere değerleri atadık ve çalıştırdık


"""
Yukarıdaki Add_Contact örneğinin çıktısı aşağıdaki gibidir:

Name =  Ercan 
Surname =  Kırbıyık 
Phone Number =  099999 
Email Address =  ercan@kirbiyik.com

"""




"""
    RETURN İFADESİ
        Değer döndürme işlemi yapar
        Değeri değişkene atayabilir ve başka bir fonksiyon veya işlemde kullanabiliriz
"""

def Sum(a, b, c, d):
    print("Toplam = ", a + b + c + d)

def Multiply(a):
    print("Multiply = ", a * a)

Sum(12, 5, 9, 2)

Multiply(3)

"""
Yukarıda Sum() ve Multiply() fonksiyonları ayrı ayrı çalışmaktadır Fakat bunları Return ifadesi olmadan

Multiply(Sum(1,2,3,4)) 

şeklinde çalıştırırsak hata alacaktır çünkü Sum() fonksiyonunun çıktısını kaydetmemektedir ve işlemden sonra hemen silmektedir.

Aşağıdaki iki fonksiyona return koyarak işlem yaparsak çalışacaktır.

"""


def Sum2(a, b, c, d):
    print("Toplam 2 = ", a + b + c + d)
    return a + b + c + d

def Multiply2(a):
    print("Multiply 2 = ", a * a)
    return a * a

Multiply2(Sum2(12, 5, 9, 2))        # Bu işlemde önce sayıları Sum() fonksiyonunun işleminden geçirip daha sonra
                                    # Multiply fonksiyonundaki işlemleri yapacaktır ve bize sonucu verecektir.



def Multiply3(a):
    return a * 3
def Sum3(a):
    return a + 5
def Quarter(a):
    return a / 4

print("Sonuç 1 : ", Quarter(Sum3(Multiply3(7))))

print("Sonuç 2 : ", Multiply3(Quarter(Sum3(Multiply3(20)))))