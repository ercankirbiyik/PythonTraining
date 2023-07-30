"""
    MODÜLLER

    Modüller Python kodlarımızı bir mantık çerçevesinde düzenlememizi sağlar.
    Bazı işlevleri kullanabileceğimiz bir takım fonksiyonları ve nitelikleri içerisinde barındıran çerçevelerdir.
        Math, Random, Type gibi pythonda hazır modüller bulunmaktadır.


    Daha önce oluşturduğumuz bir kodu modülde gruplamak kodun okunmasını ve kullanımını kolaylaştırır.
    Modül = Python kodundan oluşan bir dosyadır.
    Pythonda modüller çok önemlidir.
"""

"""
    import ifadesi herhangi bir python kaynak dosyasını kullanmamızı sağlar.
    
    import Modül İsmi şeklinde çalışır

"""


#Math kütüphanesindeki bütünfonksiyonları çağırmamızı sağlar
import math

# Burada Math kütüphanesinden sadece factorial fonksiyonunu import ettik ve sadece onu kullanacağımızı belirttik.
from math import factorial

print(factorial(4))
