    # STRİNGLER
        # Karakter dizisidir
        # Yazı
        # Değer atamak yeterlidir
        # tek '' ya da çift "" tırnak içeriside yer alır

print("***** Örnek1 *****")
A = "Python"
print(type(A))
B = 'Ercan'
print(type(B))

print("***** Örnek2 *****")

String = 'Ercan'
print(String[0])
print(String[1])
print(String[2])
print(String[3])
print(String[4])
# ÇIKTI:
# E
# r
# c
# a
# n

print("*********")

print(String[-1])
print(String[-2])
print(String[-3])
print(String[-4])
print(String[-5])
# ÇIKTI:
#n
#a
#c
#r
#E

print("***** Örnek3 *****")

String2 = "Hakkari is a beautiful city"
print(String2[:])
print(String2[3:17])

print("***** Örnek4 *****")

# len() metodu ile stringin uzunluğunu alabiliyoruz

print(len(String))
print(len(String2))

print("***** Örnek5 *****")

# strip() metodu ile stringin başındaki ve sonundaki boşlukları kaldırabiliriz

String3 = "         Hakkari is a beautiful city           "
print(String3.strip())

# strip() metodunun içine kaldırılmasını istediğimiz değerleri yazarsak kaldırır

print("<<<<<<<Hakkari...<<<<".strip("<"))


print("***** Örnek6 *****")

# lower() metodu ile harfleri küçük olacak şekilde yazdırabiliriz
print("HAKKARI".lower())

# upper() metodu ile harfleri büyük olacak şekilde yazdırabiliriz
print("hakkari".upper())

# replace() metodu ile kelimeler veya harfler değiştirilebilir
print("Istanbul is the capital city of Turkey".replace("Istanbul", "Ankara"))