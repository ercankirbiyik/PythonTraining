"""
    LİSTE METODLARI :
        * append()   : Eleman ekleme
        * count()    : Eleman sayma
        * extend()   : Liste ekleme
        * index()    : indeks öğrenme
        * insert()   : Eleman ekleme
        * pop()      : Eleman silme
        * remove()   : Eleman silme
        * sort()     : Sıralama

"""

MyList = [1,2,3,4,5,6,7,8]
print(MyList)


# append() örneği
MyList.append(8)
print("Eleman eklenmesiyle oluşan yeni liste :", MyList) #[1, 2, 3, 4, 5, 6, 7, 8, 8]


# count() örneği
MyList.count(8)
print("Listedeki adedi :", MyList.count(8)) #2


# remove() örneği
MyList.remove(8)
print("Eleman silinmesiyle oluşan yeni liste :", MyList) #[1, 2, 3, 4, 5, 6, 7, 8]


# extend() örneği
MyList2 = [9, 10, 11, 12]
MyList.extend(MyList2)
print("Liste eklenmesiyle oluşan yeni liste :", MyList) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# index() örneği
MyList.index(11) # Listedeki 11. elemanı verir
print(MyList.index(11)) # 10


# insert() örneği
MyList3 = ["apple", "orange", "banana", "pear"]
print(MyList3)

MyList3.insert(2,"lemon") # indexi 2 olan alana "lemon" elemanını ekler ve diğer elemanları kaydırır.
print("Eleman eklenmesiyle oluşan yeni liste :", MyList3)


# pop() örneği
print("Listenin ilk hali :", MyList)
MyList.pop() #pop() metodunun içine eleman vermediğimiz için son elemanı silecektir ve çıktı olarak son elemanın indeksini verecektir.
print("Eleman silindikten sonra yeni liste :", MyList)

print("*****************")
print("Listenin ilk hali :", MyList)
print("Silinen elemanın indeksi :", MyList.pop(3))
print("Eleman silindikten sonra yeni liste :", MyList)


# remove() örneği = MyList3.remove("lemon")
print("***********")
print("Listenin ilk hali :", MyList3)
print(MyList3.remove("lemon"))
print("Eleman silindikten sonra yeni liste :", MyList3)


# sort() örneği
print("************")

Numbers = [2, 4, 9, 1, 98, 33, 46, 29, 5, -13, -8]
print("Listenin ilk hali :", Numbers)
Numbers.sort()                                                # Liste elemanlarını küçükten büyüğe sıralayacaktır.
print("Listenin sort() modu ile düzenlenmiş hali :", Numbers) # [-13, -8, 1, 2, 4, 5, 9, 29, 33, 46, 98]


print("*************")

StringList = ["London", "Liverpool", "Birmingham", "Bristol", "Chelsea", "Manchester"]
print("Listenin ilk hali :", StringList)
StringList.sort()                                                   # Liste elemanlarını alfabetik olarak sıralayacaktır.
print("Listenin sort() modu ile düzenlenmiş hali :", StringList)    # ['Birmingham', 'Bristol', 'Chelsea', 'Liverpool', 'London', 'Manchester']
