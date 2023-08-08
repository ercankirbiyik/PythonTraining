"""
    İki farklı liste oluşturup listeleri birleştirme ve liste elemanlarını sıralama işlemleri.
"""

Name = ["Robin", "William", "John", "Oliver", "Mark", "Neil", "James", "Michael", "Yoko", "Jane"]

Surname = ["Hood", "Shakespeare", "Lennon", "Twist", "Twain", "Armstrong", "Dean", "Jackson", "Ono", "Doe"]

Famous = list(zip(Name, Surname))
print(Famous)

for name, surname in Famous:
    print(name, surname)