"""
    Karakter Dizileri :
        * En Temel veri yapısıdır
        * Index değerleri atanır (index[0], index[1], index[2]...)

        * Pythonda en çok kullanılan diziler : Listeler, Demetler ve Sözlükler
            * Ortak bazı işlemler : İndeksleme, Parçalama, Ekleme..
            * Hazır fonksiyonlarda bulunmaktadır : Listenin uzunluğunu bulma, en küçük veya en büyük değeri bulma gibi...


    Liste Kavramı :
        * Listeler parantez [] içine alınan ve elemanları birbirinden virgül ile ayrılan yapılardır.
        * Elemanlar aynı tipte olmak zorunda değildir. Bir liste hem integer hem de string eleman bulundurabilir.
        Liste = [1, 2, 3] ya da Liste=['Python', 'Java'] ya da Liste = [1, 'Ercan', 4, 'Java']


    Liste İşlemleri :
        * Creating a List - Liste oluşturma
        * Indexing and slicing - indexleme ve parçalama
        * Update - Güncelleme
        * Delete - Silme

"""

MyList = [1, 2, 3, 4, 5, 6, 7, 8]
print(MyList)
print(MyList[0])    # Listenin 0'ıncı elemanını yazdırıyoruz.
print(MyList[4])    # Listenin 4'üncü elemanını yazdırıyoruz.
print(MyList[-1])   # Listenin sonuncu elemanını yazdırıyoruz.
print(MyList[1:4])  # Listenin 1. 2. ve 3. elemanlarını yazdırıyoruz.


MyList2 = ["apple", "banana", "orange", "pear"]
print(MyList2)
print(MyList2[3]) # Listenin 3'üncü elemanını yazdırıyoruz.


# Listeler Stringler gibi birer karakter dizisi olduğu için aşağıdaki örnekte olduğu gibi indexleme ve parçalama yapabiliriz
# Aşağıdaki örneğin çıktısı ['H', 'e', 'l', 'l', 'o'] şeklinde olacaktır.
String = "Hello"
S_List = list(String)
print(S_List)

S_List[1] = "u"     # Listemizin 2. elemanını "u" harfi ile değiştiriyoruz.
print(S_List)       # Buradaki çıktımız ['H', 'u', 'l', 'l', 'o'] olacaktır.

del S_List[4]       # Listemizdeki 5 elemanı yani indexi 4 olan elemanı del metodu ile siliyoruz.
print(S_List)       # Buradaki çıktımız ['H', 'u', 'l', 'l'] olacaktır.