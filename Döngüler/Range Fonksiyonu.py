"""
    RANGE FONKSİYONU

        * Pythonda tanımlı bir fonksiyondur.
        * Verdiğimiz değerlerle listelere benzer bir yapı oluşturur.
        * İsteğe bağlı olarak başlangıç, bitiş ve artan sayılar dizisi oluşturur.
        * Belirli bir aralıktaki sayıları temsil etmek için kullanılabilir.
"""

A = range(0, 15)
# Range fonksiyonunun sonucunu yazdırmak için *range() yapısı kullanılır.
print("Range A değeri : ", *A)
# Eğer yıldız(*) kullanılmaz ise çıktı aşağıdaki gibi range(0, 12) olacaktır
print("Yıldız kullanılmadığında çıktı olarak alınan range değeri : ", range(0, 12))

B = range(12) # Eğer ilk parametremiz sıfır ise belirtmek zorunda değiliz.
print("Range B değeri : ", *B)


"""
Range fonksiyonu 3 farklı parametre alan bir fonksiyondur.
range(a, b, c) 
    a --> başlangıç parametresi
    b --> bitiş parametresi
    c --> artış oranı parametresi, kaçar kaçar artmasını istiyorsak c'ye o değeri vermemiz gerekir.
Range() fonksiyonu en fazla 3 tane değer alabilir. 4 değer verdiğimizde TypeError hatası verir.
"""

# 3'ten 30'a kadar olan sayıları 4er 4er arttırarak yazdırma örneği
C = range(3, 30, 4)
print("Range C değeri : ", *C)


# 100'ten 10'a kadar olan sayıları 5er 5er azaltarak yazdırma örneği
D = range(100, 10, -5)
print("Range D değeri : ", *D)


# For döngüsü içinde range() fonksiyonu kullanma örneği

for sayi in range(0, 5):
    print(sayi)