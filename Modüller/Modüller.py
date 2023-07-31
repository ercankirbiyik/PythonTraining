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

print(factorial(6))


"""
    MODÜL OLUŞTURMA
        * Local cihazımızda boş bir file oluşturup içine .py uzantılı text dosyası oluşturabiliriz ve bu dosyanın içine kendi fonksiyonlarımızı yazabiliriz.
        * Oluşturacağımız farklı bir .py uzantılı dosyamızda, bir önceki dosyamızı import ederek içindeki bütün fonksiyonları kullanabiliriz.
        * IDE'mizde proje için oluşturduğumuz bütün dosyalar ve içindeki .py uzantılı dosyalar bizim modüllerimizi oluşturmaktadır.
        * Bu dosyaları da birbirine import ederek kullanabiliyoruz.
"""
