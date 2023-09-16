"""
    İki farklı liste oluşturup listeleri birleştirme ve liste elemanlarını sıralama işlemleri.
"""

Name = ["Robin", "William", "John", "Oliver", "Mark", "Neil", "James", "Michael", "Yoko", "Jane"]
print(Name)

Surname = ["Hood", "Shakespeare", "Lennon", "Twist", "Twain", "Armstrong", "Dean", "Jackson", "Ono", "Doe"]
print(Surname)

Famous = list(zip(Name, Surname))  #Liste birleştime işlemini yapan fonksiyonumuz list(zip())
print(Famous)

# Listeleri birleştirmek için döngü kullanıyoruz
for name, surname in Famous:
    print(name, surname)