"""
Giriş yapmak isteyen kullanıcı 3 defa hatalı giriş yaparsa hata verecek bir döngü oluşturulacak
"""

# Sistemde kayıtlı ve giriş yapılması beklenen kullanıcı adı ve şifre
Sys_KullanıcıAdi = "Ercan"
Sys_Sifre = "123456"

# Yapılacak deneme sayısı
Deneme = 3


while True:
    KullanıcıAdı = input("Lütfen kullanıcı adınızı giriniz : ")
    Sifre = input("Lütfen şifrenizi giriniz : ")

    if KullanıcıAdı != Sys_KullanıcıAdi and Sifre == Sys_Sifre:
        print("Hatalı kullanıcı adı...")
        Deneme -= 1

    elif KullanıcıAdı == Sys_KullanıcıAdi and Sifre != Sys_Sifre:
        print("Hatalı şifre...")
        Deneme -= 1

    elif KullanıcıAdı != Sys_KullanıcıAdi and Sifre != Sys_Sifre:
        print("Hatalı kullanıcı adı ve şifre...")
        Deneme -= 1

    else:
        print("Başarıyla giriş yaptınız...")
        break

    if Deneme == 0:
        print("Deneme hakkınız kalmamıştır. Lütfen sistem yöneticisi ile iletişime geçiniz...")
        break