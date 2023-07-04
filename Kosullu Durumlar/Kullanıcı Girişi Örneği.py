

Sys_Kullanici_Adi = "ercankirbiyik"
Sys_Sifre = "12345"

Kullanici_Adi = input("Lütfen kullanıcı adınızı giriniz : ")
Sifre = input("Lütfen şifrenizi giriniz : ")

if Kullanici_Adi != Sys_Kullanici_Adi and Sifre == Sys_Sifre:
    print("Hatalı kullanıcı adı girdiniz!!!")
elif Kullanici_Adi == Sys_Kullanici_Adi and Sifre != Sys_Sifre:
    print("Hatalı şifre girdiniz!!!")
elif Kullanici_Adi != Sys_Kullanici_Adi and Sifre != Sys_Sifre:
    print("Hatalı kullanıcı adı ve şifre girdiniz!!!")
else:
    print("Giriş başarılı...")