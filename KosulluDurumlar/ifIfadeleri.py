"""
    IF ifadesi
        * Kodlar sırayla satır satır çalıştırılır


        ***KARAR YAPILARI***
        * Öngürülme ve önlem alma
        * True veya False durumlarında neler yapılacağını belirleme
        * Eylem belirleme

"""

Age = int(input("Please enter your age : "))

if Age < 21:
    print("You can't enter this place!!!")


Number = int(input("Please enter a number : "))

if Number < 0:
    print("Negative")


"""
    Else İfadesi
        * if içerisindeki kod bloğu çalışmadığı zaman çalışacak bloktur.
        * İf ifadesine bağımlıdır.
"""

if Age < 21:
    print("You can't enter this place!!!")
else:
    print("Welcome...")

if Number < 0:
    print("Negative!")
else:
    print("Positive!")


"""
    Elif İfadesi
    * if kullanılmadan kullanılamaz. Hata verir
    * Birden fazla ifade ve koşul için kullanılır.
    * Opsiyoneldir.
"""

Model = int(input("Please choose 1-3 : "))

if Model == 1:
    print("You choose Rolls-Royce...")
elif Model ==2:
    print("You choose Aston Martin...")
elif Model ==3:
    print("You choose Bentley...")
else:
    print("Invalid number...")
